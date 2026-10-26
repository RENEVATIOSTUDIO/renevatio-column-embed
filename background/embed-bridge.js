(() => {
  const roots=[...document.querySelectorAll('[data-rv-embed]:not([data-rv-bound])')];
  const isEditor=()=>document.documentElement.matches('.sqs-edit-mode,.sqs-edit-mode-active')||!!document.querySelector('body.sqs-edit-mode,body.sqs-edit-mode-active');
  for(const root of roots){
    root.dataset.rvBound='true';const frame=root.querySelector('iframe');
    if(root.dataset.rvEmbed!=='background')continue;
    const post=m=>frame.contentWindow?.postMessage({rv:'background-host-v1',...m},'*');
    const configure=()=>{
      const css=getComputedStyle(root),read=(k,f)=>{const v=parseFloat(css.getPropertyValue(k));return Number.isFinite(v)?v:f;};
      post({type:'configure',scale:read('--rv-field-scale',1),x:read('--rv-field-x',0),y:read('--rv-field-y',0),
        noise:read('--rv-noise-opacity',.39),fit:css.getPropertyValue('--rv-field-fit').trim()||'auto',
        mobile:matchMedia('(max-width:639px),(pointer:coarse)').matches,static:isEditor()});
    };
    let lastPointer=null,pending=false;
    const sendPointer=e=>{
      if(e.target?.closest?.('[data-rv-embed="controls"]'))return;
      const r=frame.getBoundingClientRect();
      const inside=e.clientX>=r.left&&e.clientX<=r.right&&e.clientY>=r.top&&e.clientY<=r.bottom;
      lastPointer={type:'pointer',x:(e.clientX-r.left)/Math.max(1,r.width),y:1-(e.clientY-r.top)/Math.max(1,r.height),
        pointerType:e.pointerType||'mouse',active:inside&&e.type!=='pointercancel'&&(e.pointerType!=='touch'||e.type!=='pointerup')};
      if(!pending){pending=true;requestAnimationFrame(()=>{pending=false;if(!isEditor())post(lastPointer);});}
    };
    for(const type of ['pointermove','pointerdown','pointerup','pointercancel'])window.addEventListener(type,sendPointer,{passive:true});
    window.addEventListener('blur',()=>post({type:'pointer',x:.5,y:.5,pointerType:'mouse',active:false}));
    document.documentElement.addEventListener('pointerleave',()=>post({type:'pointer',x:.5,y:.5,pointerType:'mouse',active:false}));
    frame.addEventListener('load',configure);
    const ro=new ResizeObserver(configure);ro.observe(root);
    const mo=new MutationObserver(configure);mo.observe(root,{attributes:true,attributeFilter:['style','class']});
    mo.observe(document.documentElement,{attributes:true,attributeFilter:['class']});
    if(document.body)mo.observe(document.body,{attributes:true,attributeFilter:['class']});
    window.addEventListener('resize',configure,{passive:true});configure();
  }
  if(window.__rvEmbedRelayV1)return;
  window.__rvEmbedRelayV1=true;
  window.addEventListener('message',e=>{
    const msg=e.data;if(!msg||msg.rv!=='background-v1'||msg.relay)return;
    const frames=[...document.querySelectorAll('[data-rv-embed] iframe')];
    if(!frames.some(f=>f.contentWindow===e.source))return;
    for(const frame of frames)if(frame.contentWindow!==e.source)frame.contentWindow.postMessage({...msg,relay:true},'*');
  });
})();
