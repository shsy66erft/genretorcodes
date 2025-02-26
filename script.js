document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();
    document.querySelector(".success-message").style.display = "block";
    this.reset();
});