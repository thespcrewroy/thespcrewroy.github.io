// Taskbar clock + footer year
(function () {
  const clock = document.getElementById("clock");
  const tick = () => {
    if (!clock) return;
    clock.textContent = new Date().toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
  };
  tick();
  setInterval(tick, 15000);
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
