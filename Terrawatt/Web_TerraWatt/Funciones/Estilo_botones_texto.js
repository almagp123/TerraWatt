
// document.querySelectorAll('.factura-section').forEach((section) => {
//     section.addEventListener('click', function () {
//         const modal = document.getElementById('modal');
//         const title = document.getElementById('modal-title');
//         const text = document.getElementById('modal-info');
//         const subinfoContainer = document.getElementById('modal-subinfo');

//         // Verifica si los atributos existen
//         const titleText = this.getAttribute('data-title');
//         const mainText = this.getAttribute('data-info');
//         const subinfoText = this.getAttribute('data-subinfo');

//         // Actualiza el título y texto principal
//         title.textContent = titleText || "Sin título"; 
//         text.textContent = mainText || "Sin contenido"; 
//         const paragraphs = mainText.split('\n');
//                 text.innerHTML = ''; 
//                 paragraphs.forEach(paragraph => {
//                     if (paragraph.trim() !== '') {
//                         const p = document.createElement('p');
//                         const isBold = paragraph.includes(':');
//                         if (isBold) {
//                             const [boldText, normalText] = paragraph.split(':');
//                             const b = document.createElement('b');
//                             b.textContent = boldText + ':' ;
//                             p.appendChild(b);
//                             p.append(' ' + normalText.trim());
//                         } else {
//                             p.textContent = paragraph.trim();
//                         }
//                         text.appendChild(p);
//                     }
//                 });
//         // Generar los subapartados
//         if (subinfoText) {
//             const subinfoItems = subinfoText.split(','); // Divide los subapartados por coma
//             subinfoContainer.innerHTML = ''; // Limpia el contenedor
//             subinfoItems.forEach(item => {
//                 const li = document.createElement('li');
//                 li.textContent = item.trim();
//                 subinfoContainer.appendChild(li);
//             });
//         } else {
//             subinfoContainer.innerHTML = ''; // Limpia si no hay subinfo
//         }

//         // Mostrar el modal
//         modal.style.display = 'flex';
//     });
// });

// // Cerrar el modal
// document.querySelector('.close').addEventListener('click', function () {
//     document.getElementById('modal').style.display = 'none';
// });



// document.addEventListener("DOMContentLoaded", () => {
//     document.querySelectorAll('.factura-section').forEach((section) => {
//         section.addEventListener('click', function () {
//             const modal = document.getElementById('modal');
//             const title = document.getElementById('modal-title');
//             const text = document.getElementById('modal-info');
//             const subinfoContainer = document.getElementById('modal-subinfo');

//             // Obtener atributos del modal
//             const titleText = this.getAttribute('data-title') || "Sin título";
//             const mainText = this.getAttribute('data-info') || "Sin contenido disponible.";
//             const subinfoText = this.getAttribute('data-subinfo') || "";

//             // ✅ Actualizar el título
//             title.innerHTML = titleText; 

//             // ✅ Procesar el contenido del modal y conservar formato
//             const paragraphs = mainText.split('\n');
//             text.innerHTML = ''; 
//             paragraphs.forEach(paragraph => {
//                 if (paragraph.trim() !== '') {
//                     const p = document.createElement('p');
                    
//                     // ✅ Si hay ":", separar en negrita y texto normal
//                     if (paragraph.includes(':')) {
//                         const [boldText, normalText] = paragraph.split(':');
//                         const b = document.createElement('b');
//                         b.textContent = boldText.trim() + ':'; 
//                         p.appendChild(b);
//                         p.append(' ' + normalText.trim());
//                     } else {
//                         p.textContent = paragraph.trim();
//                     }

//                     text.appendChild(p);
//                 }
//             });

//             // ✅ Generar la lista de subinformación
//             if (subinfoText) {
//                 const subinfoItems = subinfoText.split(','); 
//                 subinfoContainer.innerHTML = ''; 
//                 const ul = document.createElement('ul');

//                 subinfoItems.forEach(item => {
//                     const li = document.createElement('li');
//                     li.textContent = item.trim();
//                     ul.appendChild(li);
//                 });

//                 subinfoContainer.appendChild(ul);
//             } else {
//                 subinfoContainer.innerHTML = ''; 
//             }

//             // ✅ Mostrar el modal
//             modal.style.display = 'flex';
//         });
//     });

//     // ✅ Cerrar el modal con el botón de cierre
//     document.querySelector('.close').addEventListener('click', function () {
//         document.getElementById('modal').style.display = 'none';
//     });

//     // ✅ Cerrar el modal con la tecla Escape
//     document.addEventListener("keydown", (event) => {
//         if (event.key === "Escape") {
//             document.getElementById('modal').style.display = 'none';
//         }
//     });
// });



document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.factura-section').forEach((section) => {
        // ✅ Permitir abrir el modal con Clic
        section.addEventListener('click', function () {
            openModal(this);
        });

        // ✅ Permitir abrir el modal con Teclado (Enter o Espacio)
        section.addEventListener('keydown', function (event) {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault(); // Evita que la página se desplace con Espacio
                openModal(this); // ✅ Pasa el elemento correcto
            }
        });
    });

    function openModal(section) {
        const modal = document.getElementById('modal');
        const title = document.getElementById('modal-title');
        const text = document.getElementById('modal-info');
        const subinfoContainer = document.getElementById('modal-subinfo');

        // Obtener atributos del modal
        const titleText = section.getAttribute('data-title') || "Sin título";
        const mainText = section.getAttribute('data-info') || "Sin contenido disponible.";
        const subinfoText = section.getAttribute('data-subinfo') || "";

        // ✅ Actualizar el título
        title.innerHTML = titleText; 

        // ✅ Procesar el contenido del modal y conservar formato
        const paragraphs = mainText.split('\n');
        text.innerHTML = ''; 
        paragraphs.forEach(paragraph => {
            if (paragraph.trim() !== '') {
                const p = document.createElement('p');
                
                // ✅ Si hay ":", separar en negrita y texto normal
                if (paragraph.includes(':')) {
                    const [boldText, normalText] = paragraph.split(':');
                    const b = document.createElement('b');
                    b.textContent = boldText.trim() + ':'; 
                    p.appendChild(b);
                    p.append(' ' + normalText.trim());
                } else {
                    p.textContent = paragraph.trim();
                }

                text.appendChild(p);
            }
        });

        // ✅ Generar la lista de subinformación
        if (subinfoText) {
            const subinfoItems = subinfoText.split(','); 
            subinfoContainer.innerHTML = ''; 
            const ul = document.createElement('ul');

            subinfoItems.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item.trim();
                ul.appendChild(li);
            });

            subinfoContainer.appendChild(ul);
        } else {
            subinfoContainer.innerHTML = ''; 
        }

        // ✅ Mostrar el modal
        modal.style.display = 'flex';
        modal.setAttribute("aria-hidden", "false");

        // ✅ Mover el foco al botón de cierre para accesibilidad
        document.querySelector('.close').focus();
    }

    // ✅ Cerrar el modal con el botón de cierre
    document.querySelector('.close').addEventListener('click', function () {
        closeModal();
    });

    // ✅ Cerrar el modal con la tecla Escape
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeModal();
        }
    });

    function closeModal() {
        const modal = document.getElementById('modal');
        modal.style.display = 'none';
        modal.setAttribute("aria-hidden", "true");

        // ✅ Devolver el foco al elemento que activó el modal
        if (lastFocusedElement) {
            lastFocusedElement.focus();
        }
    }
});
