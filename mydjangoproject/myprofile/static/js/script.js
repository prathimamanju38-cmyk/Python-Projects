
// Dark and Light Mode

const themeBtn = document.getElementById("themeBtn");

themeBtn.addEventListener("click", function() {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        themeBtn.innerHTML = "☀️";
    } else {
        themeBtn.innerHTML = "🌙";
    }

});


// Contact Form

const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;

    document.getElementById("response").innerText =
        "Thank you, " + name + "! Your message was received.";

    contactForm.reset();

});


// Welcome Message

window.addEventListener("load", function() {

    console.log("Welcome to M Prathima's Portfolio!");

});
