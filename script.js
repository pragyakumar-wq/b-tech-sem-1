// Question card par click (ya Enter / Space) karne par answer wala page khulta hai
document.querySelectorAll('[data-page]').forEach(function (card) {
  card.addEventListener('click', function () {
    window.location.href = card.dataset.page;
  });

  card.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      window.location.href = card.dataset.page;
    }
  });
});

// Exam page: tick karne par question done mark hota hai (browser mein save rehta hai)
(function () {
  var boxes = document.querySelectorAll('input.done');
  if (!boxes.length) return;
  var progress = document.getElementById('progress');

  function update() {
    var done = 0;
    boxes.forEach(function (b) {
      b.closest('li').classList.toggle('checked', b.checked);
      if (b.checked) done++;
    });
    if (progress) progress.textContent = done + ' / ' + boxes.length + ' questions done';
  }

  boxes.forEach(function (b) {
    try { b.checked = localStorage.getItem('exam-' + b.dataset.id) === '1'; } catch (e) {}
    b.addEventListener('change', function () {
      try { localStorage.setItem('exam-' + b.dataset.id, b.checked ? '1' : '0'); } catch (e) {}
      update();
    });
  });
  update();
})();
