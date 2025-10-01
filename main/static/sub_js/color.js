// 색상 토글 버튼 → 열고 닫기
document.querySelector(".color-toggle").addEventListener("click", function () {
  var section = document.querySelector(".color-section");
  section.classList.toggle("active");
});

// 색상 버튼 클릭 → 상품 필터링
var colorButtons = document.querySelectorAll(".color-list button");
var products = document.querySelectorAll("[data-color]");  // data-color 가진 모든 상품 div

for (var i = 0; i < colorButtons.length; i++) {
  colorButtons[i].addEventListener("click", function () {
    var color = this.classList[0]; // 버튼 클래스명이 색상명
    var isActive = this.classList.contains("selected");

    if (isActive) {
      // 다시 클릭 → 전체 상품 보이기
      for (var j = 0; j < products.length; j++) {
        products[j].style.display = "block";
      }
      for (var k = 0; k < colorButtons.length; k++) {
        colorButtons[k].classList.remove("selected");
      }
    } else {
      // 해당 색상만 보이기
      for (var j = 0; j < products.length; j++) {
        if (products[j].dataset.color === color) {
          products[j].style.display = "block";
        } else {
          products[j].style.display = "none";
        }
      }

      // 버튼 상태 갱신
      for (var k = 0; k < colorButtons.length; k++) {
        colorButtons[k].classList.remove("selected");
      }
      this.classList.add("selected");
    }
  });
}
