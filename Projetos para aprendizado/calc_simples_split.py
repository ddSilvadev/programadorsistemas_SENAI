#Calculadora um pouco mais avançada pegando input em uma linha unica e usando .split() para criar um array 


while True:
    entrada = input("Digite a operação (ex: 10 + 5): ")

    partes = entrada.split()

    #.split() separa cada elemento do input dentro de um array: ["10", "+", "5"]
    #index [0] -> primeiro numero
    #index [1] -> operador
    #index [2] -> segundo numero

    numero1 = float(partes[0])
    operador = partes[1]
    numero2 = float(partes[2])

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            print("Não é possível dividir por 0")
            continue
        resultado = numero1 / numero2
    elif operador == "**":
        resultado = numero1 ** numero2
    elif operador == "%":
        resultado = numero1 % numero2
    else:
        print("Operador inválido")
        continue

    print("Resultado:", resultado)



#Problemas:
#input é SEMPRE: numero operator numero. Se o input não for formatado corretamente (ex: 10+5, abc + 5, 10 + invés do esperado 10 + 5), o programa irá crashar
#Se o input for maior ou menor que 3 partes, o programa irá crashar
