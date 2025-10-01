document.querySelectorAll(".size-toggle").forEach(button => {
  button.addEventListener("click", () => {
    const section = button.parentElement;
    section.classList.toggle("active"); 
  });
});