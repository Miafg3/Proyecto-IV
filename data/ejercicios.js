export const ejercicios = [
    {
        id: 1,
        titulo: "Coste total de un viaje",
        descripcion: "Calcula el coste total de un viaje sumando alojamiento, alimentación y entretenimiento.",

        javascript: `
    const alojamiento = 200;
    const alimentacion = 150;
    const entretenimiento = 100;

    const total = alojamiento + alimentacion + entretenimiento;
    console.log("El coste total del viaje es " + total + "€");
    `,

        python: `
    alojamiento = 200
    alimentacion = 150
    entretenimiento = 100

    total = (alojamiento + alimentacion + entretenimiento)
    print(f"El coste total del viaje es {total}€")
    `,
    },

    {
        id: 2,
        titulo: "Edad de perro en años humanos",
        descripcion: "Convierte la edad de un perro a años humanos multiplicando la edad del perro por 7.",

        javascript: `
    const edadPerro = 5;
    const edadHumana = edadPerro * 7;

    console.log("La edad del perro en años humanos es " + edadHumana +" años");
    `,

        python: `
    edad_perro = 5
    edad_humana = (edad_perro * 7)

    print(f"La edad del perro en años humanos es {edad_humana} años")
    `,
    },

    {
        id: 3,
        titulo: "Calculadora de IMC",
        descripcion: "Calcula el Índice de Masa Corporal y muestra su clasificación.",

        javascript: `
    const peso = 70;
    const altura = 1.75;

    const imc = peso / (altura * altura);

    let clasificacion = "";

    if(imc < 18.5){
        clasificacion = "Bajo peso";
    }
    else if(imc < 25){
        clasificacion = "Normal";
    }
    else if(imc < 30){
        clasificacion = "Sobrepeso";
    }
    else{
        clasificacion = "Obesidad";

    }

    console.log("IMC: " + imc.toFixed(2));
    console.log("Clasificación: " + clasificacion);
    `,

        python: `
    peso = 70
    altura = 1.75

    imc = (peso / (altura ** 2))

    if imc < 18.5:
        clasificacion = "Bajo peso"

    elif imc < 25:
        clasificacion = "Normal"

    elif imc < 30:
        clasificacion = "Sobrepeso"

    else:
        clasificacion = "Obesidad"

    print(
        f"IMC: {imc:.2f}"
    )

    print(f"Clasificación: {clasificacion}")
    `,
    },
];