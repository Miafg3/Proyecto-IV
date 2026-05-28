import { ejercicios } from "./data/ejercicios.js";

const listaEjercicios = document.getElementById("lista-ejercicios");

function crearCards() {
    ejercicios.forEach((ejercicio) => {
        const card = document.createElement("article");
        card.classList.add("card");

        const titulo = document.createElement("h2");
        titulo.textContent = ejercicio.titulo;

        const descripcion = document.createElement("p");
        descripcion.textContent = ejercicio.descripcion;

        const boton = document.createElement("button");
        boton.textContent = "Ver solución";

        boton.addEventListener("click", () => {
            mostrarEjercicio(ejercicio.id);
        });

        card.appendChild(titulo);
        card.appendChild(descripcion);
        card.appendChild(boton);
        listaEjercicios.appendChild(card);
    });
}

function mostrarEjercicio(id) {
    const ejercicio = ejercicios.find((item) => item.id === id);

    document.getElementById("titulo-ejercicio").textContent = ejercicio.titulo;
    document.getElementById("descripcion-ejercicio").textContent = ejercicio.descripcion;
    document.getElementById("codigo-js").textContent = ejercicio.javascript;
    document.getElementById("codigo-python").textContent = ejercicio.python;
}

crearCards();