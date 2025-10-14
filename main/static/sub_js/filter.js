document.querySelectorAll(".filter-toggle").forEach(button => {
  button.addEventListener("click", () => {
    const section = button.parentElement;
    section.classList.toggle("active"); 
  });
});


//-------------------------------------------------------------------------
// 맨 위로 올라가는 스크롤 버튼 - JS
//-------------------------------------------------------------------------

window.addEventListener("scroll", () => {
    const btn = document.getElementById("back-to-top");
    if (window.scrollY > 100) {
        btn.classList.add("visible");
    } else {
        btn.classList.remove("visible");
    }
    });

    // 버튼 클릭하면 맨 위로 부드럽게 이동.
    document.getElementById("back-to-top").addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
    });


