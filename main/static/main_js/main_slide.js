
/* --------------------------------------------------------------- */
/* Main Slider */
/* --------------------------------------------------------------- */
const swiper1 = new Swiper(".mySwiper1", {
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: ".swiper-button-next1",
        prevEl: ".swiper-button-prev1",
    },
    allowTouchMove: false,
});


/* --------------------------------------------------------------- */
/* 추석 이벤트 상품 */
/* --------------------------------------------------------------- */
var swiper2 = new Swiper(".mySwiper2", {
        loop:true,
      navigation: {
            nextEl: ".swiper-button-next2",
            prevEl: ".swiper-button-prev2",
        },
      breakpoints: {
        1024: {
        slidesPerView: 4,
        spaceBetween: 35,
        },
      },
      allowTouchMove: false,
    });

/* --------------------------------------------------------------- */
/* 옷 카테고리 */
/* --------------------------------------------------------------- */
    var swiper3 = new Swiper(".mySwiper3", {
      loop: true,
      slidesPerView: 3,
      grid: {
        rows: 2,
      },
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
      spaceBetween: 40,
    });

   const swiperInner = new Swiper('.mySwiperInner', {
    loop: true,
    autoplay: {
      delay: 2000,
      disableOnInteraction: false,
    },
    slidesPerView: 1,
    effect: 'fade',
  });


/* --------------------------------------------------------------- */
/* 쿠폰 / 이벤트 Slider */
/* --------------------------------------------------------------- */
var swiper = new Swiper(".mySwiper4", {
      loop: true,
      effect: "flip",
      grabCursor: true,
      pagination: {
        el: ".swiper-pagination",
      },
      navigation: {
        nextEl: ".swiper-button-next4",
        prevEl: ".swiper-button-prev4",
      },
    });





/* --------------------------------------------------------------- */
/* 패션소품 카테고리 */
/* --------------------------------------------------------------- */
var swiper5 = new Swiper(".mySwiper5", {
      loop: true,
      slidesPerView: 3,
      grid: {
        rows: 2,
      },
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
      spaceBetween: 40,
      navigation: {
          nextEl: ".swiper-button-next5",
          prevEl: ".swiper-button-prev5",
      },
    });

   const swiperInner1 = new Swiper('.mySwiperInner1', {
    loop: true,
    autoplay: {
      delay: 2000,
      disableOnInteraction: false,
    },
    slidesPerView: 1,
    effect: 'fade',
  });





/* --------------------------------------------------------------- */
/* 잡화 카테고리 */
/* --------------------------------------------------------------- */
var swiper6 = new Swiper(".mySwiper6", {
      loop: true,
      slidesPerView: 3,
      grid: {
        rows: 2,
      },
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
      spaceBetween: 40,
      navigation: {
          nextEl: ".swiper-button-next6",
          prevEl: ".swiper-button-prev6",
      },
    });

   const swiperInner2 = new Swiper('.mySwiperInner2', {
    loop: true,
    autoplay: {
      delay: 2000,
      disableOnInteraction: false,
    },
    slidesPerView: 1,
    effect: 'fade',
  });
