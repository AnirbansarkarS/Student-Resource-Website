//chiabrata works
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


// Example GSAP animation on page load
gsap.from("#text h1", {
  opacity: 0,
  y: 100,
  duration: 1,
  ease: "power3.out"
});

gsap.from("#text p", {
  opacity: 0,
  y: 50,
  duration: 1,
  delay: 0.3,
  ease: "power3.out"
});
