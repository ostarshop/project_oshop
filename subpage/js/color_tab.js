// 까딱이 연결ㅠ
document.querySelectorAll(".color-toggle").forEach(button => {
  button.addEventListener("click", () => {
    const section = button.parentElement;
    section.classList.toggle("active"); 
  });
});