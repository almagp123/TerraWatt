document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const modalText = document.getElementById("modal-text");
    const closeBtn = document.querySelector(".close");
    const sections = document.querySelectorAll(".factura-section");

    // Abrir modal al hacer clic en una sección
    sections.forEach(section => {
        section.addEventListener("click", () => {
            modalText.textContent = section.getAttribute("data-info");
            modal.style.display = "flex";
        });
    });

    // Cerrar modal al hacer clic en la "X"
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Cerrar modal al hacer clic fuera del contenido
    window.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});