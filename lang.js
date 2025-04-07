document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("langToggle");
    let currentLang = "he";

    toggleBtn.addEventListener("click", () => {
        currentLang = currentLang === "he" ? "en" : "he";
        document.documentElement.lang = currentLang;
        document.documentElement.dir = currentLang === "he" ? "rtl" : "ltr";
        toggleBtn.textContent = currentLang === "he" ? "English" : "עברית";

        document.querySelectorAll("[data-lang-he]").forEach(el => {
            el.textContent = el.getAttribute(`data-lang-${currentLang}`);
        });
    });
});