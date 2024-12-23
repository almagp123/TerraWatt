
document.querySelectorAll('.factura-section').forEach((section) => {
    section.addEventListener('click', function () {
        const modal = document.getElementById('modal');
        const title = document.getElementById('modal-title');
        const text = document.getElementById('modal-info');
        const subinfoContainer = document.getElementById('modal-subinfo');

        // Verifica si los atributos existen
        const titleText = this.getAttribute('data-title');
        const mainText = this.getAttribute('data-info');
        const subinfoText = this.getAttribute('data-subinfo');

        // Actualiza el título y texto principal
        title.textContent = titleText || "Sin título"; // Default si no hay título
        text.textContent = mainText || "Sin contenido"; // Default si no hay texto principal
        const paragraphs = mainText.split('\n');
                text.innerHTML = ''; 
                paragraphs.forEach(paragraph => {
                    if (paragraph.trim() !== '') {
                        const p = document.createElement('p');
                        const isBold = paragraph.includes(':');
                        if (isBold) {
                            const [boldText, normalText] = paragraph.split(':');
                            const b = document.createElement('b');
                            b.textContent = boldText + ':' ;
                            p.appendChild(b);
                            p.append(' ' + normalText.trim());
                        } else {
                            p.textContent = paragraph.trim();
                        }
                        text.appendChild(p);
                    }
                });
        // Generar los subapartados
        if (subinfoText) {
            const subinfoItems = subinfoText.split(','); // Divide los subapartados por coma
            subinfoContainer.innerHTML = ''; // Limpia el contenedor
            subinfoItems.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item.trim();
                subinfoContainer.appendChild(li);
            });
        } else {
            subinfoContainer.innerHTML = ''; // Limpia si no hay subinfo
        }

        // Mostrar el modal
        modal.style.display = 'flex';
    });
});

// Cerrar el modal
document.querySelector('.close').addEventListener('click', function () {
    document.getElementById('modal').style.display = 'none';
});

