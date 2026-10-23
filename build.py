"""Prepare a static Pages site and refresh the nine image copies.

Edit projects.json to replace any image or destination. No dependencies needed.
"""
from pathlib import Path
import argparse
import concurrent.futures
import hashlib
import json
import shutil
import struct
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent


def build(local_images=None, preview=False):
    projects = json.loads((ROOT / 'projects.json').read_text())
    if len(projects) != 9:
        raise ValueError('projects.json must contain exactly nine projects')
    for item in projects:
        for field in ('image', 'link'):
            if urllib.parse.urlparse(item[field]).scheme != 'https':
                raise ValueError(f'{field} must be an HTTPS URL: {item[field]}')
    site = ROOT / '_site'
    (site / 'assets').mkdir(parents=True, exist_ok=True)
    (site / 'vendor').mkdir(exist_ok=True)

    def prepare(pair):
        index, project = pair
        name = Path(urllib.parse.unquote(urllib.parse.urlparse(project['image']).path)).name
        if local_images:
            data = (Path(local_images) / name).read_bytes()
        else:
            request = urllib.request.Request(project['image'], headers={'User-Agent':'RENEVATIO-ImageSync/1.0'})
            with urllib.request.urlopen(request, timeout=45) as response:
                data = response.read(16 * 1024 * 1024 + 1)
        if len(data) > 16 * 1024 * 1024:
            raise ValueError(f'Image {index+1} exceeds 16 MB')
        if data.startswith(b'\x89PNG\r\n\x1a\n'):
            extension = 'png'
            width, height = struct.unpack('>II', data[16:24])
        elif data.startswith(b'\xff\xd8'):
            extension, width, height = 'jpg', None, None
        elif data[:4] == b'RIFF' and data[8:12] == b'WEBP':
            extension, width, height = 'webp', None, None
        else:
            raise ValueError(f'Image {index+1} must be PNG, JPEG, or WebP')
        digest = hashlib.sha256(data).hexdigest()[:12]
        relative = f'assets/project-{index+1:02d}-{digest}.{extension}'
        (site / relative).write_bytes(data)
        return {**project, 'texture':relative}, {'card':index+1,'bytes':len(data),'width':width,'height':height,'sha256':hashlib.sha256(data).hexdigest()}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        prepared = list(pool.map(prepare, enumerate(projects)))
    for name in ('index.html','.nojekyll'):
        shutil.copyfile(ROOT / name, site / name)
    for name in ('three.module.js','THREE-LICENSE.txt'):
        shutil.copyfile(ROOT / 'vendor' / name, site / 'vendor' / name)
    (site / 'projects.json').write_text(json.dumps([item for item,_ in prepared],indent=2,ensure_ascii=False)+'\n')
    if preview:
        shutil.copyfile(ROOT / 'preview.html', site / 'preview.html')
    (ROOT / 'build-report.json').write_text(json.dumps([report for _,report in prepared],indent=2)+'\n')
    print(f'Built {len(prepared)} projects in {site}')
    for _, report in prepared:
        print(f"  {report['card']}: {report['width']} × {report['height']}, {report['bytes']} bytes")


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--local-images', help='Use supplied source files for offline preview')
    parser.add_argument('--preview', action='store_true')
    args=parser.parse_args()
    build(args.local_images,args.preview)
