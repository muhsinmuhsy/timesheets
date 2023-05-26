// Add active class to clicked menu item
var navItems = document.querySelectorAll('nav ul li a');

navItems.forEach(function(item) {
  item.addEventListener('click', function() {
    navItems.forEach(function(item) {
      item.classList.remove('active');
    });
    this.classList.add('active');
  });
});


