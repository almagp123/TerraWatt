// // // document.addEventListener("DOMContentLoaded", () => {
// // //     const modal = document.getElementById("modal");
// // //     const modalText = document.getElementById("modal-text");
// // //     const closeBtn = document.querySelector(".close");
// // //     const sections = document.querySelectorAll(".factura-section");

// // //     // Abrir modal al hacer clic en una sección
// // //     sections.forEach(section => {
// // //         section.addEventListener("click", () => {
// // //             modalText.textContent = section.getAttribute("data-info");
// // //             modal.style.display = "flex";
// // //         });
// // //     });

// // //     // Cerrar modal al hacer clic en la "X"
// // //     closeBtn.addEventListener("click", () => {
// // //         modal.style.display = "none";
// // //     });

// // //     // Cerrar modal al hacer clic fuera del contenido
// // //     window.addEventListener("click", (e) => {
// // //         if (e.target === modal) {
// // //             modal.style.display = "none";
// // //         }
// // //     });
// // // });




// // document.addEventListener("DOMContentLoaded", () => {
// //     const modal = document.getElementById("modal");
// //     const modalText = document.getElementById("modal-text");

// //     const closeBtn = document.querySelector(".close");
// //     const sections = document.querySelectorAll(".factura-section");

// //     let lastFocusedElement;

// //     function openModal(section) {
// //         lastFocusedElement = document.activeElement;
// //         modal.style.display = "flex";
// //         modal.setAttribute("aria-hidden", "false");

// //         closeBtn.focus(); // Mover el foco al botón de cierre
// //     }

// //     function closeModal() {
// //         modal.style.display = "none";
// //         modal.setAttribute("aria-hidden", "true");

// //         if (lastFocusedElement) {
// //             lastFocusedElement.focus(); // Devuelve el foco a la sección que activó el modal
// //         }
// //     }

// //     // Abrir modal con clic o teclado
// //     sections.forEach(section => {
// //         section.addEventListener("click", () => openModal(section));

// //         section.addEventListener("keydown", (event) => {
// //             if (event.key === "Enter" || event.key === " ") {
// //                 openModal(section);
// //             }
// //         });
// //     });

// //     // Cerrar modal con click en la "X"
// //     closeBtn.addEventListener("click", closeModal);

// //     // ✅ Cerrar modal con `Enter` o `Espacio` en la "X"
// //     closeBtn.addEventListener("keydown", (event) => {
// //         if (event.key === "Enter" || event.key === " ") {
// //             closeModal();
// //         }
// //     });

// //     // Cerrar modal con `Esc`
// //     window.addEventListener("keydown", (event) => {
// //         if (event.key === "Escape") {
// //             closeModal();
// //         }
// //     });

// //     // Cerrar modal al hacer clic fuera del contenido
// //     window.addEventListener("click", (e) => {
// //         if (e.target === modal) {
// //             closeModal();
// //         }
// //     });
// // });
// document.addEventListener("DOMContentLoaded", () => {
//     const modal = document.getElementById("modal");
//     const modalTitle = document.getElementById("modal-title");
//     const modalInfo = document.getElementById("modal-info");
//     const modalSubinfo = document.getElementById("modal-subinfo");
//     const closeBtn = document.querySelector(".close");
//     const sections = document.querySelectorAll(".factura-section");
//     const modalText = document.getElementById("modal-text");

//     let lastFocusedElement;

//     function openModal(section) {
//         lastFocusedElement = document.activeElement; // Guarda el elemento que tenía el foco

//         // ✅ Se cambia `textContent` por `innerHTML` para mantener formato
//         // modalTitle.innerHTML = section.getAttribute("data-title") || "Sin título";
//         // modalInfo.innerHTML = section.getAttribute("data-info") || "Sin información disponible.";
//         // modalSubinfo.innerHTML = section.getAttribute("data-subinfo") || "";
//         modalText.textContent = section.getAttribute("data-info");

//         modal.style.display = "flex";
//         modal.setAttribute("aria-hidden", "false");

//         closeBtn.focus(); // Mueve el foco a la "X"
//     }

//     function closeModal() {
//         modal.style.display = "none";
//         modal.setAttribute("aria-hidden", "true");

//         if (lastFocusedElement) {
//             lastFocusedElement.focus(); // Regresa el foco a la sección que lo activó
//         }
//     }

//     // Abrir modal con clic o teclado
//     sections.forEach(section => {
//         section.addEventListener("click", () => openModal(section));

//         section.addEventListener("keydown", (event) => {
//             if (event.key === "Enter" || event.key === " ") {
//                 event.preventDefault(); // Evita que la página se desplace al presionar espacio
//                 openModal(event.currentTarget); // ✅ Se asegura que pase el elemento correcto
//             }
//         });
//     });

//     // Cerrar modal con click en la "X"
//     closeBtn.addEventListener("click", closeModal);

//     // ✅ Cerrar modal con `Enter` o `Espacio` en la "X"
//     closeBtn.addEventListener("keydown", (event) => {
//         if (event.key === "Enter" || event.key === " ") {
//             closeModal();
//         }
//     });

//     // Cerrar modal con `Esc`
//     window.addEventListener("keydown", (event) => {
//         if (event.key === "Escape") {
//             closeModal();
//         }
//     });

//     // Cerrar modal al hacer clic fuera del contenido
//     window.addEventListener("click", (e) => {
//         if (e.target === modal) {
//             closeModal();
//         }
//     });
// });




document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const modalTitle = document.getElementById("modal-title");
    const modalInfo = document.getElementById("modal-info");
    const modalSubinfo = document.getElementById("modal-subinfo");
    const closeBtn = document.querySelector(".close");
    const sections = document.querySelectorAll(".factura-section");

    let lastFocusedElement;

    function openModal(section) {
        lastFocusedElement = document.activeElement; // Guarda el foco actual

        modalTitle.innerHTML = section.getAttribute("data-title") || "Sin título";
        modalInfo.innerHTML = section.getAttribute("data-info") || "Sin información disponible.";
        modalSubinfo.innerHTML = section.getAttribute("data-subinfo") || "";

        modal.style.display = "flex";
        modal.setAttribute("aria-hidden", "false");

        closeBtn.focus(); // Mueve el foco al botón de cierre
    }

    function closeModal() {
        modal.style.display = "none";
        modal.setAttribute("aria-hidden", "true");

        if (lastFocusedElement) {
            lastFocusedElement.focus(); // Regresa el foco al elemento que activó el modal
        }
    }

    // ✅ Se asegura que los elementos sean navegables con teclado
    sections.forEach(section => {
        section.setAttribute("tabindex", "0"); // Hace que sea seleccionable con Tab
        section.setAttribute("role", "button"); // Indica que es un elemento interactivo

        // ✅ Abrir modal con clic
        section.addEventListener("click", () => openModal(section));

        // ✅ Abrir modal con "Enter" o "Espacio"
        section.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault(); // Evita que Espacio haga scroll
                openModal(section); // ✅ Se pasa directamente la sección
            }
        });
    });

    // ✅ Cerrar modal con clic en la "X"
    closeBtn.addEventListener("click", closeModal);

    // ✅ Cerrar modal con "Enter" o "Espacio" en la "X"
    closeBtn.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
            closeModal();
        }
    });

    // ✅ Cerrar modal con "Esc"
    window.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeModal();
        }
    });

    // ✅ Cerrar modal al hacer clic fuera del contenido
    window.addEventListener("click", (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
});

