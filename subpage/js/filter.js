document.querySelectorAll(".filter-toggle").forEach(button => {
  button.addEventListener("click", () => {
    const section = button.parentElement;
    section.classList.toggle("active"); 
  });
});