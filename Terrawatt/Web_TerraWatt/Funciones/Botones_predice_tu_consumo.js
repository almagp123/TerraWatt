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
  
// Array con las provincias (esto puede expandirse según lo que necesites)
const provincias = [
  "Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga", 
  "Murcia", "Palma", "Las Palmas", "Bilbao", "Alicante", "Córdoba"
];

// Obtener el select por su ID
const selectProvincia = document.getElementById("provincia");

// Añadir las opciones dinámicamente
provincias.forEach(provincia => {
  selectProvincia.innerHTML += `<option value="${provincia.toLowerCase().replace(" ", "-")}">${provincia}</option>`;
});


  












// function enviarDatos() {
//   const potencia = document.getElementById("potencia").value;
//   const numero_residentes = document.getElementById("numero_residentes").value;
//   const tipo_vivienda = document.getElementById("tipo_vivienda").value;
//   const provincia = document.getElementById("provincia").value;
//   const mes = document.getElementById("mes").value;  // Nuevo campo para el mes

//   const datos = {
//       potencia: parseFloat(potencia),
//       numero_residentes: parseInt(numero_residentes),
//       tipo_vivienda: tipo_vivienda,
//       provincia: provincia,
//       mes: mes  // Se añade el mes al objeto
//   };

//   fetch("http://127.0.0.1:8000/transformar", {
//       method: "POST",
//       headers: {
//           "Content-Type": "application/json",
//       },
//       body: JSON.stringify(datos),
//   })
//   .then((response) => response.json())
//   .then((data) => {
//       // Seleccionar el contenedor donde se mostrarán los resultados
//       const resultadoDiv = document.getElementById("resultado");

//       // Crear un contenido dinámico basado en los datos transformados
//       const resultadosHTML = `
//           <p><strong>Potencia:</strong> ${data.datos_transformados.potencia}</p>
//           <p><strong>Número de Residentes:</strong> ${data.datos_transformados.numero_residentes}</p>
//           <p><strong>Tipo de Vivienda:</strong> ${data.datos_transformados.tipo_vivienda}</p>
//           <p><strong>Provincia:</strong> ${data.datos_transformados.provincia}</p>
//           <p><strong>Mes:</strong> ${data.datos_transformados.mes}</p>  <!-- Se muestra el mes -->
//       `;

//       // Insertar los resultados en el contenedor
//       resultadoDiv.innerHTML = resultadosHTML;
//   })
//   .catch((error) => {
//       console.error("Error:", error);
//       document.getElementById("resultado").innerHTML = 
//           "<p style='color: red;'>Hubo un error al procesar los datos.</p>";
//   });
 
// }
function enviarDatos() {
  const potencia = document.getElementById("potencia").value;
  const numero_residentes = document.getElementById("numero_residentes").value;
  const tipo_vivienda = document.getElementById("tipo_vivienda").value;
  const provincia = document.getElementById("provincia").value;
  const mes = document.getElementById("mes").value;

  // Definir las variables dummy basadas en la selección del tipo de vivienda
  let tipoViviendaDummy = {
    "Tipo de vivienda_Casa Unifamiliar": false,
    "Tipo de vivienda_Duplex": false,
    "Tipo de vivienda_Piso": false
  };

  // Actualizar el valor a true basado en la selección del usuario
  if (tipo_vivienda === "Casa Unifamiliar") {
    tipoViviendaDummy["Tipo de vivienda_Casa Unifamiliar"] = true;
  } else if (tipo_vivienda === "Duplex") {
    tipoViviendaDummy["Tipo de vivienda_Duplex"] = true;
  } else if (tipo_vivienda === "Piso") {
    tipoViviendaDummy["Tipo de vivienda_Piso"] = true;
  }

  // Crear el objeto de datos con los valores correctos
  const datos = {
      potencia: parseFloat(potencia),
      numero_residentes: parseInt(numero_residentes),
      tipo_vivienda: tipo_vivienda,
      provincia: provincia,
      mes: parseInt(mes),
      ...tipoViviendaDummy  // Agregar las variables dummy al objeto
  };

  // Verificar si todos los campos tienen valores válidos
  if (!provincia || !mes || !potencia || !numero_residentes || !tipo_vivienda) {
    alert("Por favor, completa todos los campos.");
    return;
  }

  fetch("http://127.0.0.1:8000/transformar", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify(datos),
  })
  .then((response) => response.json())
  .then((data) => {
      // Seleccionar el contenedor donde se mostrarán los resultados
      const resultadoDiv = document.getElementById("resultado");

      // Crear un contenido dinámico basado en los datos transformados
      const resultadosHTML = `
          <p><strong>Potencia:</strong> ${data.datos_transformados.potencia}</p>
          <p><strong>Número de Residentes:</strong> ${data.datos_transformados.numero_residentes}</p>
          <p><strong>Tipo de Vivienda:</strong> ${data.datos_transformados.tipo_vivienda}</p>
          <p><strong>Provincia:</strong> ${data.datos_transformados.provincia}</p>
          <p><strong>Mes:</strong> ${data.datos_transformados.mes}</p>  <!-- Se muestra el mes -->
      `;

      // Insertar los resultados en el contenedor
      resultadoDiv.innerHTML = resultadosHTML;
  })
  .catch((error) => {
      console.error("Error:", error);
      document.getElementById("resultado").innerHTML = 
          "<p style='color: red;'>Hubo un error al procesar los datos.</p>";
  });
}
