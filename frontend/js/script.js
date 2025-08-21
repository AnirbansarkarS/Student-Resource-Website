var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,       // show 3 cards at a time
  spaceBetween: 30,       // gap between cards
  grabCursor: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
