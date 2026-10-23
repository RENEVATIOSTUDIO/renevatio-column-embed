# RENEVATIO vertical 3D project column

One external page embedded in one Squarespace 7.1 **Embed Block**. No JavaScript or Code Injection is required inside Squarespace. The external page runs Three.js and custom shaders. The existing Squarespace page is not modified by this repository.

## Replace an image or destination

Edit `projects.json`. It contains exactly nine records in the order supplied by Stephen. Every record has:

- `name`: the project name used for keyboard access.
- `image`: the original Squarespace image URL.
- `link`: the click destination; initially `https://www.renevatio.studio/` for all nine.

Commit the settings file. GitHub Actions fetches fresh image copies, gives them content-hashed filenames, and redeploys GitHub Pages. This avoids the duplicate cross-origin headers returned by the supplied Squarespace image host. Image changes are not made by editing the embed snippet.

## Reference measurements

The footer WebGL column on `https://mondragon.framer.website/` is the motion reference. Its published layout settings were inspected on 2026-10-22. The unrelated four-card rotor in the process section is not the reference.

| Setting | Value |
|---|---|
| Reference card count | 8 |
| RENEVATIO card count | 9 |
| Card canvas, before 3D projection | 6 × 8 scene units; exactly 3:4 |
| Angular speed | −2π/24 radians/second (same direction) |
| Full turn | 24 seconds |
| Camera distance / vertical FOV | 52 scene units / 40° |
| Gap | 0.2 scene units |
| Bend | 0.8, corresponding to a 48° cylindrical arc |
| Vertical step / wave amplitude | −3.1 / 1.3 scene units |
| Hover rotation speed | 9% of normal, with smooth approach/return |
| Entire-card hover scale | 1.09 from its center |
| Starting phase | 0.19 radians, matching Stephen's supplied startup screenshot |
| Orb border | Lovable color stops; 1.69 CSS pixels; 8-second turn |

Pixel dimensions change continuously with perspective and editable block dimensions. There is no single fixed projected pixel width or height for a moving card. The underlying canvases are all 6 × 8 units. The complete scene is fitted uniformly to contain all nine cards, including maximum hover growth, within the iframe.

The outline uses a genuine fourth-order superellipse shader and the same outline for hit testing. It does not use CSS `border-radius`. The original reference uses a quadratic corner mask; the superellipse fulfills Stephen's explicit true-squircle requirement. Card curvature, vertical positions, camera perspective, and direction follow the measured reference settings. The 24-second turn and revised hover settings are Stephen's approved updates. The formation inversion was canceled; all images remain upright. Reverse faces use mirrored texture coordinates so logos stay readable, with a narrow whole-image blend within roughly two degrees of the card center turning edge-on. Motion starts at the supplied pose after all image loads settle, rather than advancing during loading.

The rotating rim uses the existing Lovable stylesheet's `--orb-rim-stops`, `--carousel-orb-rim-width: 1.69px`, `135deg` starting angle, and `rim-spin 8s linear`. It is rendered along the true squircle boundary. Reduced-motion mode freezes both the column and the rotating rim; enlargement and links remain available.

## Squarespace installation

Copy all of `squarespace-embed.html` into one **Embed Block → Code snippet → Embed Data**. The file contains the verified public hosting URL: https://renevatiostudio.github.io/renevatio-column-embed/ .

Resize and place the outer block in Fluid Engine. Its internal canvas has no minimum size, uses the available width and height, and fits its 3D envelope uniformly. Target the actual Squarespace block ID in existing desktop/mobile CSS to set absolute position, width, height, and stacking. The snippet does not set page-level positioning or z-index.

The outer block can overlap the next section using the user's existing CSS; the renderer contains its own cards within that block. Page section clipping, if any, is controlled by the existing Squarespace layout.

The snippet switches to a static preview and disables iframe pointer interception under Squarespace's `.sqs-edit-mode` or `.sqs-edit-mode-active` classes. The hidden live iframe stops through its visibility observer. That rule must be verified in the actual Squarespace editor after insertion; this local build cannot certify the live editor's markup or plan behavior.

Squarespace documents Embed Blocks on all plans, including manual embed code. Arbitrary external iframe acceptance on the user's exact plan must be confirmed in that block. HTML/JavaScript/iframe features in a Code Block have different plan restrictions. No Squarespace billing or subscription changes are made by this project.

## Build and local review

`python3 build.py --preview` prepares `_site/` and refreshes image copies from the URLs. Use `--local-images /absolute/path` to use supplied originals offline. Serve `_site/` with a local HTTP server. `preview.html` offers local canvas-size, static-motion, and editor-mode checks.

## Publishing

Published with Stephen’s explicit approval to [RENEVATIOSTUDIO/renevatio-column-embed](https://github.com/RENEVATIOSTUDIO/renevatio-column-embed). The verified live page is [the RENEVATIO project column](https://renevatiostudio.github.io/renevatio-column-embed/). A public GitHub repository supports Pages on GitHub Free. Only this widget, its image copies, and its source settings are published. The Squarespace site itself has not been edited.

Sources: [reference](https://mondragon.framer.website/), [Squarespace embeds](https://support.squarespace.com/hc/en-us/articles/206543617-Embed-blocks), [Three.js](https://threejs.org/).
