/*let numero1 = parseInt(prompt("ingrese el primer numero"));
let numero3 = parseInt(prompt("ingrese el segundo numero"));
let suma = numero1 + numero3;

//console.log(suma);
//alert("la suma es: "+ suma)


document.getElementById("suma").innerHTML = "la suma es: "+ suma;*/
function sumar () {
    let numero1 = document.getElementById("numero1").value;
    let numero2 = document.getElementById("numero2").value;
    let suma = parseInt(numero1) + parseInt(numero2);
    document.getElementById("resultado").innerHTML = "la suma es: " + suma;
}