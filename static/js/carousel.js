
(function(){
  function initCarousel(root){
    const track = root.querySelector('.carousel-track');
    const slides = Array.from(root.querySelectorAll('.slide'));
    const prev = root.querySelector('.prev');
    const next = root.querySelector('.next');
    const dotsWrap = root.querySelector('.dots');

    let index = 0;
    slides.forEach((_, i) => {
      const b = document.createElement('button');
      b.setAttribute('aria-label', 'Go to slide ' + (i+1));
      if(i===0) b.classList.add('active');
      dotsWrap.appendChild(b);
      b.addEventListener('click', ()=>goTo(i));
    });

    function goTo(i){
      index = Math.max(0, Math.min(i, slides.length-1));
      const slide = slides[index];
      slide.scrollIntoView({behavior:'smooth', inline:'center', block:'nearest'});
      Array.from(dotsWrap.children).forEach((d,di)=>{
        d.classList.toggle('active', di===index);
      });
    }
    function nextSlide(){ goTo(index+1 >= slides.length ? 0 : index+1); }
    function prevSlide(){ goTo(index-1 < 0 ? slides.length-1 : index-1); }

    next.addEventListener('click', nextSlide);
    prev.addEventListener('click', prevSlide);

    // Drag / Touch
    let startX = 0, scrollStart = 0, isDown = false;
    function onDown(e){
      isDown = true;
      startX = (e.touches ? e.touches[0].clientX : e.clientX);
      scrollStart = track.scrollLeft;
      track.classList.add('dragging');
    }
    function onMove(e){
      if(!isDown) return;
      const x = (e.touches ? e.touches[0].clientX : e.clientX);
      const dx = x - startX;
      track.scrollLeft = scrollStart - dx;
    }
    function onUp(){
      if(!isDown) return;
      isDown = false;
      track.classList.remove('dragging');
      // snap to nearest slide
      let best = 0, bestDist = Infinity;
      slides.forEach((s, i)=>{
        const rect = s.getBoundingClientRect();
        const center = rect.left + rect.width/2;
        const viewportCenter = window.innerWidth/2;
        const d = Math.abs(center - viewportCenter);
        if(d < bestDist){ bestDist = d; best = i; }
      });
      goTo(best);
    }
    track.addEventListener('mousedown', onDown);
    track.addEventListener('mousemove', onMove);
    document.addEventListener('mouseup', onUp);
    track.addEventListener('touchstart', onDown, {passive:true});
    track.addEventListener('touchmove', onMove, {passive:true});
    track.addEventListener('touchend', onUp);

    // Observe scroll to update index
    const obs = new IntersectionObserver((entries)=>{
      entries.forEach(ent=>{
        if(ent.isIntersecting){
          const i = slides.indexOf(ent.target);
          if(i >= 0){
            index = i;
            Array.from(dotsWrap.children).forEach((d,di)=>d.classList.toggle('active', di===index));
          }
        }
      });
    }, { root: track, threshold: 0.6 });
    slides.forEach(s=>obs.observe(s));
  }

  document.querySelectorAll('[data-carousel]').forEach(initCarousel);
})();
