// פונקציה להחלפת שפה
const langToggleButton = document.getElementById('langToggle');
const elements = document.querySelectorAll('[data-lang-he], [data-lang-en]');

langToggleButton.addEventListener('click', () => {
    const currentLang = document.documentElement.lang === 'he' ? 'he' : 'en';
    const newLang = currentLang === 'he' ? 'en' : 'he';
    document.documentElement.lang = newLang;
    elements.forEach(element => {
        const text = element.getAttribute(`data-lang-${newLang}`);
        element.innerHTML = text;
    });

    langToggleButton.innerHTML = newLang === 'he' ? 'English' : 'עברית';
});

// קביעת השפה המתחילה
if (document.documentElement.lang !== 'he') {
    document.documentElement.lang = 'en';
    elements.forEach(element => {
        const text = element.getAttribute('data-lang-en');
        element.innerHTML = text;
    });
    langToggleButton.innerHTML = 'עברית';
}