const toggleDropdown = (list) => {
    const currentElementWithShow = document.querySelector(".show");
    if (currentElementWithShow) {
      currentElementWithShow.classList.toggle("show");
    }
    if (list) {
      list.classList.toggle("show");
    }
  }
  
  const dropBtns = document.querySelectorAll(".dropbtn");
  
  dropBtns.forEach(dropBtn => {
    dropBtn.addEventListener("click", () => {
      toggleDropdown(dropBtn.nextElementSibling);
    });
  });
  
  window.addEventListener("click", (e) =>{
    if(!e.target.matches('.dropbtn')) {
      toggleDropdown();
    }
  });