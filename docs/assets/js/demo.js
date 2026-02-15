// Simple simulated demo: generates devices, updates status, and handles actions
(function(){
  function randInt(max){return Math.floor(Math.random()*max)}
  const devices = Array.from({length:6}).map((_,i)=>({
    id:`dev-${1000+i}`,
    name:`device-${i+1}`,
    os: ['linux','windows','mac'][randInt(3)],
    cpu: randInt(80)+5,
    mem: randInt(80)+5,
    online: Math.random() > 0.15
  }));

  const listEl = document.getElementById('device-list');
  const detailEl = document.getElementById('device-detail');
  let selected = null;

  function renderList(){
    listEl.innerHTML = '';
    devices.forEach(d=>{
      const li = document.createElement('li');
      li.className = 'device-item';
      li.tabIndex = 0;
      li.innerHTML = `<strong>${d.name}</strong> <span class="muted">${d.os}</span> <span class="badge ${d.online? 'up':'down'}">${d.online? 'online':'offline'}</span>`;
      li.onclick = ()=> selectDevice(d.id);
      li.onkeypress = (e)=>{ if(e.key==='Enter') selectDevice(d.id) };
      listEl.appendChild(li);
    });
  }

  function selectDevice(id){
    selected = devices.find(x=>x.id===id);
    if(!selected) return;
    detailEl.innerHTML = `<h4>${selected.name}</h4>
      <p class="muted">${selected.id} — ${selected.os}</p>
      <p>CPU: ${selected.cpu}% • Memory: ${selected.mem}%</p>
      <pre class="device-log">Last check: ${new Date().toLocaleTimeString()}</pre>`;
  }

  function updateStatuses(){
    devices.forEach(d=>{
      // small random fluctuations
      d.cpu = Math.max(1, Math.min(99, d.cpu + (Math.random()-0.5)*8));
      d.mem = Math.max(1, Math.min(99, d.mem + (Math.random()-0.5)*6));
      if(Math.random() < 0.03) d.online = !d.online;
    });
    renderList();
    if(selected) selectDevice(selected.id);
  }

  document.getElementById('cmd-restart').addEventListener('click', ()=>{
    if(!selected){ alert('Select a device first'); return }
    const log = detailEl.querySelector('.device-log');
    log.textContent += `\n[${new Date().toLocaleTimeString()}] Restart command sent.`;
    // show a simulated status change
    selected.online = false;
    setTimeout(()=>{ selected.online = true; updateStatuses(); log.textContent += `\n[${new Date().toLocaleTimeString()}] Device back online.`; }, 1400 + Math.random()*1600);
    renderList();
  });

  document.getElementById('cmd-collect').addEventListener('click', ()=>{
    if(!selected){ alert('Select a device first'); return }
    const log = detailEl.querySelector('.device-log');
    log.textContent += `\n[${new Date().toLocaleTimeString()}] Collected diagnostics (simulated).`;
  });

  // initial render
  renderList();
  // pick first device
  selectDevice(devices[0].id);
  // periodic updates
  setInterval(updateStatuses, 2500);

})();
