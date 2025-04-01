// אתחול AOS
AOS.init({
  duration: 1000,
  once: true
});

// אנימציה על תוכן ההירו
gsap.from(".hero-content", { 
  opacity: 0, 
  y: 50, 
  duration: 1.5, 
  ease: "power3.out" 
});

// גלילה חלקה בעת לחיצה על קישורי הניווט
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    if (targetId.startsWith("#")) {
      gsap.to(window, { 
        duration: 1, 
        scrollTo: targetId, 
        ease: "power2.out" 
      });
    }
  });
});