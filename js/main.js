const phrases = [
  { text: 'loosening its collar.', src: 'Dezeen · 2026' },
  { text: 'done with the immaculate render.', src: 'Dezeen · 2026' },
  { text: 'getting warmer, darker, more expressive.', src: 'Dwell · 2026' },
  { text: 'choosing tactility over seamless finishes.', src: 'Dwell · 2026' },
  { text: 'welcoming ornament back.', src: 'Dwell · 2026' },
  { text: 'a system now, not a screen.', src: 'mean.ceo · 2026' },
  { text: 'a brief that machines can read.', src: 'Design.md · 2026' },
  { text: 'directing intent, not executing tasks.', src: 'Architectural Record · 2026' },
  { text: 'making room for imperfection.', src: 'Dezeen · 2026' },
  { text: 'having its purple moment.', src: 'Business of Home · 2026' },
];

function initPhraseRotation() {
  const phraseEl = document.getElementById('phrase');
  const sourceEl = document.getElementById('phrase-source');
  let index = 0;

  setInterval(() => {
    phraseEl.style.opacity = 0;
    sourceEl.style.opacity = 0;
    setTimeout(() => {
      index = (index + 1) % phrases.length;
      phraseEl.textContent = phrases[index].text;
      sourceEl.textContent = 'From the design press · ' + phrases[index].src;
      phraseEl.style.opacity = 1;
      sourceEl.style.opacity = 1;
    }, 450);
  }, 30000);
}

function initFilterChips() {
  const chips = document.querySelectorAll('.chip');
  const bands = document.querySelectorAll('.project-band');
  const countEl = document.getElementById('count');
  const total = bands.length;

  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      chips.forEach(c => c.classList.remove('is-active'));
      chip.classList.add('is-active');

      const cat = chip.dataset.cat;
      let visibleCount = 0;
      bands.forEach(band => {
        const match = cat === 'All' || band.dataset.cat.split(' ').includes(cat);
        band.style.display = match ? '' : 'none';
        if (match) visibleCount++;
      });

      countEl.textContent = formatCount(visibleCount, total);

      // Bring the first matching project into view if the visitor is already past the filter bar.
      const filterBar = document.getElementById('work');
      if (filterBar.getBoundingClientRect().top <= parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav-h'))) {
        filterBar.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  countEl.textContent = formatCount(total, total);
}

function formatCount(n, total) {
  return String(n).padStart(2, '0') + ' / ' + String(total).padStart(2, '0');
}

// Keep sticky offsets in sync with the real nav + filter bar heights (they change at breakpoints).
function initStickyOffsets() {
  const root = document.documentElement;
  const nav = document.querySelector('.nav');
  const filterBar = document.querySelector('.filter-bar');
  const update = () => {
    const navH = nav.offsetHeight;
    root.style.setProperty('--nav-h', navH + 'px');
    root.style.setProperty('--stack-top', navH + filterBar.offsetHeight + 'px');
  };
  update();
  window.addEventListener('resize', update);
  if (document.fonts) document.fonts.ready.then(update);
}

// Bands whose image hasn't been added yet get a designed placeholder instead of an empty block.
function initBandImages() {
  document.querySelectorAll('.project-band').forEach((band, i) => {
    const bg = band.style.backgroundColor || getComputedStyle(band).backgroundColor;
    band.dataset.tone = isLight(bg) ? 'light' : 'dark';

    const index = document.createElement('div');
    index.className = 'project-band__index';
    index.setAttribute('aria-hidden', 'true');
    index.textContent = String(i + 1).padStart(2, '0');
    band.appendChild(index);

    const imageEl = band.querySelector('.project-band__image');
    if (imageEl && imageEl.querySelector('img')) return; // composed from <img> elements
    const match = imageEl && imageEl.style.backgroundImage.match(/url\(["']?(.*?)["']?\)/);
    if (!match) { band.classList.add('is-placeholder'); return; }
    const probe = new Image();
    probe.onerror = () => band.classList.add('is-placeholder');
    probe.onload = () => {
      // Never upscale: if the source can't cover the panel at 2x density, show it at native
      // sharpness (natural px / 2) centered on the panel's background instead of stretching it.
      if (probe.naturalWidth < band.clientWidth * 2) {
        const img = document.createElement('img');
        img.src = probe.src;
        img.alt = '';
        img.style.maxWidth = Math.round(probe.naturalWidth / 2) + 'px';
        imageEl.style.backgroundImage = 'none';
        imageEl.classList.add('project-band__image--native');
        imageEl.appendChild(img);
      }
    };
    probe.src = match[1];
  });
}

function isLight(color) {
  const m = color.match(/\d+/g);
  if (!m) return true;
  const [r, g, b] = m.map(Number);
  return (0.299 * r + 0.587 * g + 0.114 * b) > 150;
}

// Case study pages don't exist yet; disable links that would 404 instead of sending visitors to an error page.
function initCaseStudyLinks() {
  document.querySelectorAll('.project-band').forEach(band => {
    const href = band.getAttribute('href');
    const disable = () => {
      band.setAttribute('aria-disabled', 'true');
      band.removeAttribute('href');
      const cta = band.querySelector('.project-band__cta');
      if (cta) cta.textContent = 'Case study coming soon';
    };
    if (!href || href.startsWith('#')) return;
    fetch(href.split('?')[0], { method: 'HEAD' })
      .then(res => { if (!res.ok) disable(); })
      .catch(disable);
  });
}

initStickyOffsets();
initBandImages();
initCaseStudyLinks();
initPhraseRotation();
initFilterChips();
