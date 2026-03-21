document.addEventListener("DOMContentLoaded", function () {
  const toggles = document.querySelectorAll(".js-expand-toggle");

  toggles.forEach((button) => {
    button.addEventListener("click", function () {
      const wrapper = button.closest(".expandable-text-wrapper");
      const text = wrapper.querySelector(".js-expandable-text");

      text.classList.toggle("is-expanded");
      button.textContent = text.classList.contains("is-expanded")
        ? "Ver menos"
        : "Leer más";
    });
  });

  const revealItems = document.querySelectorAll(".js-reveal");

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
          }
        });
      },
      { threshold: 0.12 }
    );

    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  }
});