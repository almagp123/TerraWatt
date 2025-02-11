// // Esperamos a que se carge todala página para ejecutar el scripr, y accedemos el elementoque el id "toggleAccesible", por otro lado creamos un boton en el cual podamos activaro desactivar este elemento, y creamos una función que lea el texto, es español, con un volumen1, a la velocidad especificada... 
// document.addEventListener("DOMContentLoaded", function () {
//     const toggleAccesible = document.getElementById("toggleAccesible");
//     toggleAccesible.addEventListener("click", function () {
//         document.body.classList.toggle("modo-accesible");
//     });
//     window.leerTexto = function (id) {
//         // let texto = document.getElementById(id).innerText;
//         let texto = document.getElementById(id).textContent;
//         let speech = new SpeechSynthesisUtterance();
//         speech.text = texto;
//         speech.lang = "es-ES";
//         speech.rate = 1;
//         speech.volume = 1;
//         window.speechSynthesis.speak(speech);
//     };
// });

// // document.addEventListener("DOMContentLoaded", function () {
// //     const toggleAccesible = document.getElementById("toggleAccesible");
// //     toggleAccesible.addEventListener("click", function () {
// //         document.body.classList.toggle("modo-accesible");
// //     });

// //     window.leerTexto = function (id) {
// //         // let texto = document.getElementById(id).textContent;
// //         // let speech = new SpeechSynthesisUtterance();
// //         let texto = document.getElementById(id).textContent;
// //         let speech = new SpeechSynthesisUtterance();

// //         speech.text = texto;

// //         // Detecta el idioma del documento y ajusta la voz
// //         let idioma = document.documentElement.lang;
// //         if (idioma === "en") {
// //             speech.lang = "en-US"; // Inglés americano
// //         } 
// //         if (idioma === "es") {
// //             speech.lang = "es-ES"; // Inglés americano
// //         } 
// //         else {
// //             speech.lang = "es-ES"; // Español de España
// //         }

// //         speech.rate = 1;
// //         speech.volume = 1;
// //         window.speechSynthesis.speak(speech);
// //     };
// // });
document.addEventListener("DOMContentLoaded", function () {
    const toggleAccesible = document.getElementById("toggleAccesible");
    toggleAccesible.addEventListener("click", function () {
        document.body.classList.toggle("modo-accesible");
    });

    window.leerTexto = function (id) {
        let texto = document.getElementById(id).textContent;
        let speech = new SpeechSynthesisUtterance();
        speech.text = texto;

        // Detecta el idioma del documento y ajusta la voz
        let idioma = document.documentElement.lang;
        if (idioma === "en") {
            speech.lang = "en-US"; // Inglés americano
        } else if (idioma === "ar") {
            speech.lang = "ar-SA"; // Árabe (Arabia Saudita)
        } else {
            speech.lang = "es-ES"; // Español de España
        }

        speech.rate = 1;
        speech.volume = 1;
        window.speechSynthesis.speak(speech);
    };
});

