
function cargarComponente(url, contenedorId, callback) {
    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error(`Error al cargar ${url}: ${response.status}`);
            return response.text();
        })
        .then(data => {
            document.getElementById(contenedorId).innerHTML = data;
            console.log(`✅ ${url} cargado exitosamente.`);
            if (callback) callback(); // Ejecutar el callback después de cargar
        })
        .catch(error => console.error(`❌ Error al cargar ${url}:`, error));
}

// ✅ Función para activar la lógica del botón hamburguesa
function inicializarHamburguesa() {
    console.log("✅ Lógica de la hamburguesa inicializada.");

    const hamburguesa = document.querySelector('.hamburguesa');
    const barraNav = document.querySelector('.barra-navegacion');

    if (hamburguesa && barraNav) {
        hamburguesa.addEventListener('click', () => {
            hamburguesa.classList.toggle('active');
            barraNav.classList.toggle('active');
            console.log("🍔 Menú hamburguesa activado/desactivado.");
        });

        document.addEventListener('click', (event) => {
            if (!hamburguesa.contains(event.target) && !barraNav.contains(event.target)) {
                hamburguesa.classList.remove('active');
                barraNav.classList.remove('active');
                console.log("🚪 Menú hamburguesa cerrado por clic externo.");
            }
        });
    } else {
        console.warn('⚠️ No se encontraron el botón de hamburguesa o la barra de navegación.');
    }
}

// ✅ Cargar la barra de navegación y activar la hamburguesa después de cargar
cargarComponente('Barra_navegacion.html', 'header-placeholder', inicializarHamburguesa);

// ✅ Cargar el pie de página (sin lógica adicional)
cargarComponente('Pie_de_pagina.html', 'footer-placeholder');
