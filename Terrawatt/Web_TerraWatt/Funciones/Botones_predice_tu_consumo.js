document.querySelectorAll('.boton').forEach(boton => {
    boton.addEventListener('click', () => {
      document.querySelectorAll('.boton').forEach(btn => btn.classList.remove('activo'));
      boton.classList.add('activo');
    });
});




const botonBase = document.getElementById("opcion-base");
const botonValle = document.getElementById("opcion-valle");
const seccionDesplegableBase = document.getElementById("seccion-desplegable-base");

botonBase.addEventListener("click", () => {
  botonBase.classList.add("activo");
  botonValle.classList.remove("activo");
  seccionDesplegableBase.classList.add("activo");
});

botonValle.addEventListener("click", () => {
  botonValle.classList.add("activo");
  botonBase.classList.remove("activo");
  seccionDesplegableBase.classList.remove("activo");
});




const decrementBtn = document.getElementById("decrement");
const incrementBtn = document.getElementById("increment");
const potenciaInput = document.getElementById("potencia");

// Función para decrementar el valor en pasos de 0.5
decrementBtn.addEventListener("click", () => {
  const currentValue = parseFloat(potenciaInput.value); // Asegúrate de convertir a flotante
  const minValue = parseFloat(potenciaInput.min);
  if (currentValue > minValue) {
    potenciaInput.value = (currentValue - 0.5).toFixed(1); // Resta 0.5 y mantiene un decimal
  }
});

// Función para incrementar el valor en pasos de 0.5
incrementBtn.addEventListener("click", () => {
  const currentValue = parseFloat(potenciaInput.value); // Asegúrate de convertir a flotante
  const maxValue = parseFloat(potenciaInput.max);
  if (currentValue < maxValue) {
    potenciaInput.value = (currentValue + 0.5).toFixed(1); // Suma 0.5 y mantiene un decimal
  }
});

// Selección de elementos
const decrementResidentesBtn = document.getElementById("decrement-residentes");
const incrementResidentesBtn = document.getElementById("increment-residentes");
const numeroResidentesInput = document.getElementById("numero_residentes");

// Función para decrementar el valor en pasos de 0.5
decrementResidentesBtn.addEventListener("click", () => {
  const currentValue = parseFloat(numeroResidentesInput.value); // Convertimos el valor actual a flotante
  const minValue = parseFloat(numeroResidentesInput.min);
  if (currentValue > minValue) {
    numeroResidentesInput.value = currentValue - 1; // Resta 0.5 y mantiene un decimal
  }
});

// Función para incrementar el valor en pasos de 0.5
incrementResidentesBtn.addEventListener("click", () => {
  const currentValue = parseFloat(numeroResidentesInput.value); // Convertimos el valor actual a flotante
  const maxValue = parseFloat(numeroResidentesInput.max);
  if (currentValue < maxValue) {
    numeroResidentesInput.value = currentValue + 1; // Suma 0.5 y mantiene un decimal
  }
});

