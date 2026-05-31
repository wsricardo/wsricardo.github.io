document.documentElement.classList.add("has-js");

document.addEventListener("DOMContentLoaded", () => {
    const faders = document.querySelectorAll(".fade-in");

    if ("IntersectionObserver" in window) {
        const appearOptions = {
            threshold: 0.15,
            rootMargin: "0px 0px -50px 0px"
        };

        const appearOnScroll = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    appearOnScroll.unobserve(entry.target);
                }
            });
        }, appearOptions);

        faders.forEach((fader) => {
            const rect = fader.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                fader.classList.add("visible");
            }
            appearOnScroll.observe(fader);
        });
    } else {
        faders.forEach((fader) => fader.classList.add("visible"));
    }

    const navToggle = document.querySelector(".nav-toggle");
    const mainNav = document.querySelector("#main-nav");

    if (navToggle && mainNav) {
        navToggle.addEventListener("click", () => {
            const isOpen = mainNav.classList.toggle("nav-open");
            navToggle.setAttribute("aria-expanded", String(isOpen));
        });

        mainNav.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                mainNav.classList.remove("nav-open");
                navToggle.setAttribute("aria-expanded", "false");
            });
        });
    }
});
