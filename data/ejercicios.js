export const ejercicios = [
  {
    id: 1,
    titulo: "Coste total de un viaje",
    descripcion:
      "Calcula el coste total de un viaje sumando alojamiento, alimentación y entretenimiento.",

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
    descripcion:
      "Convierte la edad de un perro a años humanos multiplicando la edad del perro por 7.",

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
    descripcion:
      "Calcula el Índice de Masa Corporal y muestra su clasificación.",

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

  {
    id: 4,
    titulo: "Calculadora de descuentos",
    descripcion:
      "Calcula el precio final de un producto después de aplicar un porcentaje de descuento.",

    javascript: `
    function calcularDescuento(precio, descuento) {
        return precio - (precio * descuento / 100);
    }

    const precio = 50;
    const descuento = 20;

    const precioFinal = calcularDescuento(precio, descuento);

    console.log("Precio final: " + precioFinal + " euros");
    `,

    python: `
    def calcular_descuento(precio, descuento):
        return precio - (precio * descuento / 100)

    precio = 50
    descuento = 20

    precio_final = (calcular_descuento(precio, descuento))
    print(f"Precio final: {precio_final} euros")
    `,
  },

  {
    id: 5,
    titulo: "Generador de números primos",
    descripcion:
      "Muestra todos los números primos comprendidos entre dos números.",

    javascript: `
    function esPrimo(numero){

        if(numero < 2){
            return false;
        }

        for(let i = 2; i < numero; i++) {
            if (numero % i === 0) {
                return false;
            }
        }
    
        return true;
    }

    const inicio = 10;
    const fin = 20;

    const primos = [];

    for(let numero = inicio; numero <= fin; numero++) {
        if(esPrimo(numero)) {
            primos.push(numero);
        }
    }

    console.log(primos.join(", "));
`,

    python: `
    def es_primo(numero):
        if numero < 2:
            return False

        for i in range(2, numero):

            if numero % i == 0:
                return False

        return True

    inicio = 10
    fin = 20

    primos = []

    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos.append(numero)

    print(primos)
`,
  },

  {
    id: 6,
    titulo: "Generador de secuencia Fibonacci",
    descripcion: "Genera los primeros N términos de la secuencia Fibonacci.",

    javascript: `
    function fibonacci(cantidad) {
        const secuencia = [0, 1];

        for(let i = 2; i < cantidad; i++) {
            secuencia.push(secuencia[i - 1] + secuencia[i - 2]);
        }

        return secuencia;
    }

    const cantidad = 8;
    const resultado = fibonacci(cantidad);

    console.log(resultado.join(", "));
`,

    python: `
    def fibonacci(cantidad):
        secuencia = [0, 1]

        for i in range(2, cantidad):

            secuencia.append(secuencia[i - 1] + secuencia[i - 2])

        return secuencia

    cantidad = 8

    resultado = fibonacci(cantidad)
    print(resultado)
`,
  },
];