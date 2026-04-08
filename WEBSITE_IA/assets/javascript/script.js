var legado = "Evite usar var, use let"; //var é a forma antiga de declarar váriaveis
let nome = "Dionata"; //variavel string
let dataNascimento = 1995; //variavel integer
let anoAtual = 2026;
let idade = anoAtual - dataNascimento;
const PI = 3.14159;//variavel constante que não irá mudar ao longo da execução do código

//para concatenar strings com string, usamos + e para concaconar integers com string usamos virgula
console.log("Olá, meu nome é "+nome+" e eu tenho ", anoAtual - dataNascimento, "anos");


if (idade < 16){
    console.log("less than 16");
}
else if (idade < 30){
    console.log("less than 30");
}
else if (idade < 50){
    console.log("less than 50")
}    
else{
    console.log("Everything else")
}


//----------------------------------

let valor1 = 20;
let valor2 = 3;

console.log("Operadores Aritiméticos: +, -, *, /, ** e %");
console.log(`Adição + ${valor1+valor2}`);
console.log(`Subtração - ${valor1-valor2}`);
console.log(`Multiplicação * ${valor1*valor2}`);
console.log(`Divisão / ${valor1/valor2}`);
console.log(`Potencia ** ${valor1**valor2}`);
console.log(`Módulo % ${valor1%valor2}`); //retorna o resto da divisão


