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


//Función valida
// ----------
// function enviarDatos() {
//   // Capturar el valor de potencia y convertirlo a número
//   const potencia = parseFloat(document.getElementById("potencia").value);
//   console.log("Potencia capturada como número:", potencia);

//   const numero_residentes = parseInt(document.getElementById("numero_residentes").value, 10);
//   const tipo_vivienda = document.getElementById("tipo_vivienda").value;
//   const provincia = document.getElementById("provincia").value;
//   const mes = parseInt(document.getElementById("mes").value);

//   // Construir el objeto para enviar
//   const datos = {
//     potencia: potencia, // Ya es un número
//     numero_residentes: numero_residentes,
//     tipo_vivienda: tipo_vivienda,
//     provincia: provincia,
//     mes: mes
//   };
//   console.log("Datos enviados al backend:", datos);

//   // Realizar el fetch
//   fetch("http://127.0.0.1:8000/transformar", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(datos),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       console.log("Respuesta recibida del backend:", data);

//       const resultadoDiv = document.getElementById("resultado");
//       const transformados = data.datos_transformados;

//       if (!transformados) {
//         console.error("Error: No se encontraron datos transformados en la respuesta del backend.");
//         return;
//       }
//       console.log("Datos transformados:", transformados);

//       // Formatear la predicción a 2 decimales y añadir la unidad "kWh"
//       const prediccionFormateada = transformados.prediccion.toFixed(2) + " kWh";

//       let resultadosHTML = `<p><strong>Predicción:</strong> ${prediccionFormateada}</p>`;

//       // Crear el CSV para descargar
//       let csvContent = "data:text/csv;charset=utf-8,";
//       csvContent += "Potencia, Número de Residentes, Provincia, Mes, Tipo de Vivienda, TMEDIA, TMIN, TMAX, VELMEDIA, SOL, PRESMAX, PRESMIN, Predicción\n";
//       csvContent += `${transformados.potencia}, ${transformados.numero_residentes}, ${transformados.provincia}, ${transformados.mes}, ${transformados.tipo_vivienda}, ${transformados.TMEDIA}, ${transformados.TMIN}, ${transformados.TMAX}, ${transformados.VELMEDIA}, ${transformados.SOL}, ${transformados.PRESMAX}, ${transformados.PRESMIN}, ${transformados.prediccion}\n`;

//       // Crear un enlace de descarga con imagen
//       const encodedUri = encodeURI(csvContent);
//       const downloadLink = document.createElement("a");
//       downloadLink.setAttribute("href", encodedUri);
//       downloadLink.setAttribute("download", "prediccion_datos.csv");



//       // Crear la imagen para el enlace
//       const imagen = document.createElement("img");
//       imagen.src = "../Web_TerraWatt/images/imagen_descarga.png"; // Asegúrate de reemplazar esta URL con la ruta de tu imagen
//       imagen.alt = "Descargar CSV";
//       imagen.style.width = "50px"; // Ajusta el tamaño de la imagen
//       imagen.style.cursor = "pointer";
//       imagen.style.alignItems = "center";

//       // Cuando la imagen se haga clic, se activará la descarga
//       downloadLink.appendChild(imagen);

//       // Mostrar el enlace con la imagen
//       resultadoDiv.innerHTML = resultadosHTML + "<br>" + downloadLink.outerHTML;
//     })
//     .catch((error) => {
//       console.error("Error al procesar la solicitud:", error);
//       document.getElementById("resultado").innerHTML =
//         "<p style='color: red;'>Hubo un error al procesar los datos.</p>";
//     });


//   }



// -----------------

function enviarDatos() {
  // Capturar los valores del formulario
  const potencia = parseFloat(document.getElementById("potencia").value);
  console.log("Potencia capturada como número:", potencia);

  const numero_residentes = parseInt(document.getElementById("numero_residentes").value, 10);
  const tipo_vivienda = document.getElementById("tipo_vivienda").value;
  const provincia = document.getElementById("provincia").value;
  const mes = parseInt(document.getElementById("mes").value);

  // Construir el objeto de datos a enviar
  const datos = {
    potencia: potencia,
    numero_residentes: numero_residentes,
    tipo_vivienda: tipo_vivienda,
    provincia: provincia,
    mes: mes
  };
  console.log("Datos enviados al backend:", datos);

  // Realizar la petición fetch
  fetch("http://127.0.0.1:8000/transformar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(datos),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Respuesta recibida del backend:", data);

      const resultadoDiv = document.getElementById("resultado");
      const transformados = data.datos_transformados;

      if (!transformados) {
        console.error("Error: No se encontraron datos transformados en la respuesta del backend.");
        resultadoDiv.innerHTML = "<p style='color: red;'>Error al obtener datos transformados.</p>";
        return;
      }
      console.log("Datos transformados:", transformados);

      // Procesar la predicción de consumo
      const consumo = transformados.prediccion_consumo;
      const consumoFormateado = consumo.toFixed(2) + " kWh";
      
      // Procesar la predicción de precio (si existe)
      let precioHTML = "";
      if (transformados.precio && typeof transformados.precio === "object") {
        const fechaInicio = transformados.precio.fecha_inicio;
        const fechaFin = transformados.precio.fecha_fin;
        const precioMedio = transformados.precio.precio_medio.toFixed(2) + " €/MWh";
        precioHTML = `<p><strong>Precio medio (de ${fechaInicio} a ${fechaFin}):</strong> ${precioMedio}</p>`;
      } else {
        precioHTML = "<p style='color: red;'>No se encontró información de precio.</p>";
      }

      // Combinar resultados
      let resultadosHTML = `<p><strong>Consumo predicho:</strong> ${consumoFormateado}</p>`;
      resultadosHTML += precioHTML;

      // (Opcional) Si deseas seguir generando el CSV, podrías incluir también los datos relacionados.
      let csvContent = "data:text/csv;charset=utf-8,";
      csvContent += "Potencia, Número de Residentes, Provincia, Mes, Tipo de Vivienda, TMEDIA, TMIN, TMAX, VELMEDIA, SOL, PRESMAX, PRESMIN, Predicción Consumo, Precio Medio\n";
      csvContent += `${transformados.potencia}, ${transformados.numero_residentes}, ${transformados.provincia}, ${transformados.mes}, ${transformados.tipo_vivienda}, ${transformados.TMEDIA}, ${transformados.TMIN}, ${transformados.TMAX}, ${transformados.VELMEDIA}, ${transformados.SOL}, ${transformados.PRESMAX}, ${transformados.PRESMIN}, ${consumo}, ${transformados.precio ? transformados.precio.precio_medio : ""}\n`;

      // Crear el enlace de descarga con imagen
      const encodedUri = encodeURI(csvContent);
      const downloadLink = document.createElement("a");
      downloadLink.setAttribute("href", encodedUri);
      downloadLink.setAttribute("download", "prediccion_datos.csv");

      const imagen = document.createElement("img");
      imagen.src = "../Web_TerraWatt/images/imagen_descarga.png";  // Ajusta la ruta si es necesario
      imagen.alt = "Descargar CSV";
      imagen.style.width = "50px";
      imagen.style.cursor = "pointer";
      imagen.style.alignItems = "center";

      downloadLink.appendChild(imagen);
      resultadoDiv.innerHTML = resultadosHTML + "<br>" + downloadLink.outerHTML;
    })
    .catch((error) => {
      console.error("Error al procesar la solicitud:", error);
      document.getElementById("resultado").innerHTML =
        "<p style='color: red;'>Hubo un error al procesar los datos.</p>";
    });
}
