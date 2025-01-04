// Función para manejar botones activos
function activarBoton(botonSeleccionado, botones) {
    botones.forEach(boton => boton.classList.remove("activo"));
    botonSeleccionado.classList.add("activo");
  }
  
  // Botones principales y su funcionalidad
  const botonesOpciones = document.querySelectorAll('.boton');
  const seccionDesplegableBase = document.getElementById("seccion-desplegable-base");
  const avisoTrabajando = document.getElementById("aviso-trabajando");
  
  botonesOpciones.forEach(boton => {
    boton.addEventListener('click', () => {
      if (boton.id === "opcion-base") {
        activarBoton(boton, botonesOpciones);
        seccionDesplegableBase.classList.add("activo");
        avisoTrabajando.classList.remove("activo");
      } else if (boton.id === "opcion-valle") {
        activarBoton(boton, botonesOpciones);
        seccionDesplegableBase.classList.remove("activo");
        avisoTrabajando.classList.add("activo");
      }
    });
  });
  
  // Función genérica para manejar incrementos y decrementos
  function manejarIncrementoDecremento(decrementBtn, incrementBtn, input, step = 1) {
    decrementBtn.addEventListener("click", () => {
      const currentValue = parseFloat(input.value);
      const minValue = parseFloat(input.min);
      if (currentValue > minValue) {
        input.value = (currentValue - step).toFixed(1);
      }
    });
  
    incrementBtn.addEventListener("click", () => {
      const currentValue = parseFloat(input.value);
      const maxValue = parseFloat(input.max);
      if (currentValue < maxValue) {
        input.value = (currentValue + step).toFixed(1);
      }
    });
  }
  
  // Manejo de los controles de incremento/decremento
  manejarIncrementoDecremento(
    document.getElementById("decrement"),
    document.getElementById("increment"),
    document.getElementById("potencia"),
    0.5
  );
  
  manejarIncrementoDecremento(
    document.getElementById("decrement-residentes"),
    document.getElementById("increment-residentes"),
    document.getElementById("numero_residentes"),
    1
  );
  
  manejarIncrementoDecremento(
    document.getElementById("decrement-consumo"),
    document.getElementById("increment-consumo"),
    document.getElementById("numero_consumo"),
    1
  );
  
  // Generar dinámicamente opciones del menú de provincias
  const provincias = [
    "Álava", "Albacete", "Alicante", "Almería", "Asturias", "Ávila", "Badajoz",
    "Barcelona", "Burgos", "Cáceres", "Cádiz", "Cantabria", "Castellón",
    "Ciudad Real", "Córdoba", "Cuenca", "Girona", "Granada", "Guadalajara",
    "Guipúzcoa", "Huelva", "Huesca", "Illes Balears", "Jaén", "La Coruña",
    "La Rioja", "Las Palmas", "León", "Lérida", "Lugo", "Madrid", "Málaga",
    "Murcia", "Navarra", "Ourense", "Palencia", "Pontevedra", "Salamanca",
    "Santa Cruz de Tenerife", "Segovia", "Sevilla", "Soria", "Tarragona",
    "Teruel", "Toledo", "Valencia", "Valladolid", "Vizcaya", "Zamora", "Zaragoza",
    "Ceuta", "Melilla"
  ];
  
  const selectProvincia = document.getElementById("provincia");
  selectProvincia.innerHTML = `<option value="">Selecciona una provincia</option>`;
  provincias.forEach(provincia => {
    selectProvincia.innerHTML += `<option value="${provincia.toLowerCase()}">${provincia}</option>`;
  });
  