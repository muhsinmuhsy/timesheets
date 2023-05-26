document.getElementById("menu-toggle").addEventListener("click", function() {
    var menuIcon = document.getElementById("menu-icon");
    if (menuIcon.classList.contains("bi-list")) {
        menuIcon.classList.remove("bi-list");
        menuIcon.classList.add("bi-x");
    } else {
        menuIcon.classList.remove("bi-x");
        menuIcon.classList.add("bi-list");
    }
});