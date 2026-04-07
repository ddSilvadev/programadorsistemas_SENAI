#Calculadora um pouco mais avançada para construir sobre a calc_simples_split.py
#nessa iteração da calculadora, foi usado o methodo next() para percorrer o input entrada e procurar se existe um operador (operadores_lista)
#uso de def, lambda e while loop

#Grande restrição dessa versão é que ainda estamos limitados há apenas numero operador numero
#nova versão deve conter algoritimo para lidar com expressoes tipo 10+5*2 ou qualquer outro modelo


def calcular(entrada):
    operacoes = {
        "+": lambda a,b: a + b,
        "-": lambda a,b: a - b,
        "**": lambda a,b: a ** b,
        "*": lambda a,b: a * b,
        "/": lambda a, b: "Erro: divisão por zero" if b == 0 else a / b,
        "%": lambda a,b: a % b 
    }
    #uma função lambda é uma funcão pequena e sem nome
    #lambda argumentos : expressão

    operador = next((op for op in operacoes if op in entrada), None)
       
    if operador is None:
        return "Operador inválido!"
    partes = entrada.split(operador) #aqui uso split() para separar o input e como delimitador é usado o {operador}, o que retorna 2 numeros em uma lista ex: ["10", "5"]
    if len(partes) != 2:
        return "Formato inválido"
    #verifica se o input é um numero, caso não for retorna erro
    try:
        numero1 = float(partes[0].strip()) #apenas o float já é o suficiente mas para tirar spaços, letras, etc. mas usar .strip() é boa prática 
        numero2 = float(partes[1].strip())
    except ValueError:
        return "Número inválido"

    return operacoes[operador](numero1, numero2)


while True:
    entrada = input("Digite a operação (ex: 10 + 5): ")
    resultado = calcular(entrada)
    print("Resultado:", resultado)