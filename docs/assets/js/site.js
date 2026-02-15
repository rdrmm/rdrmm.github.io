document.addEventListener('DOMContentLoaded',function(){
  const btn=document.getElementById('theme-toggle');
  const darkKey='rdrmm-theme-dark';
  function applyTheme(isDark){
    if(isDark) document.documentElement.classList.add('theme-dark');
    else document.documentElement.classList.remove('theme-dark');
    localStorage.setItem(darkKey, isDark? '1':'0');
    btn.textContent = isDark? '☀️' : '🌙';
  }
  // initialize from storage or system preference
  const stored = localStorage.getItem(darkKey);
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  applyTheme(stored===null ? prefersDark : stored==='1');
  btn.addEventListener('click', ()=> applyTheme(!document.documentElement.classList.contains('theme-dark')));

  // small entrance animation for hero content
  const hero = document.querySelector('.hero-copy');
  if(hero){ hero.style.opacity=0; hero.style.transform='translateY(8px)';
    setTimeout(()=>{ hero.style.transition='opacity 600ms ease, transform 600ms ease'; hero.style.opacity=1; hero.style.transform='none'; },120);
  }
});
