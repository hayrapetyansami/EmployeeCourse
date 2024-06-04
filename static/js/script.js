window.addEventListener("DOMContentLoaded", () => {
  new Swiper(".mySwiper", {
    loop: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  const languageButtons = document.querySelectorAll(".language-button");
  const languageInput = document.getElementById("language-input");

  languageButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      const language = this.value;
      languageInput.value = language;
      document.getElementById("language-form").submit();
    });
  });
});