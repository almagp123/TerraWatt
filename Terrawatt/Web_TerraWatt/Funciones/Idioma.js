function inicializarSelectorIdioma() {
    console.log("✅ Lógica del selector de idioma inicializada.");

    const idiomaBoton = document.querySelector('.idioma-boton');
    const idiomaMenu = document.querySelector('.idioma-menu');

    if (idiomaBoton && idiomaMenu) {
        idiomaBoton.addEventListener('click', (event) => {
            event.stopPropagation(); // Evita que el clic se propague y cierre inmediatamente
            idiomaMenu.classList.toggle('activo'); // Alterna la visibilidad del menú
            console.log("🌍 Selector de idioma activado/desactivado.");
        });

        // Cierra el menú cuando se hace clic fuera
        document.addEventListener('click', (event) => {
            if (!idiomaBoton.contains(event.target) && !idiomaMenu.contains(event.target)) {
                idiomaMenu.classList.remove('activo');
                console.log("🚪 Menú de idioma cerrado por clic externo.");
            }
        });
    } else {
        console.warn('⚠️ No se encontraron el botón de idioma o el menú de idioma.');
    }
}

// ✅ Cargar la barra de navegación y activar la hamburguesa e idioma después de cargar
cargarComponente('Barra_navegacion.html', 'header-placeholder', () => {
    inicializarHamburguesa();
    inicializarSelectorIdioma();
});



