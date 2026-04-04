#Calculadora

while True:
    numero1 = float(input("Insira o primeiro numero: "))
    numero2 = float(input("Insira o segundo numero: "))
    operador= input("Operator (+, -, *, /, **, %): ")

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/": #divisão
        if numero2 == 0:
            print("Não é possivel divisão por 0")
            exit()
        resultado = numero1 / numero2
    elif operador == "**": #potência
        resultado = numero1 / numero2
    elif operador == "%": #modulo: resto da divisão
        resultado = numero1 / numero2
    else:
        print("Operador inválido")
        exit()

    print("Resultado: ", resultado)

    denovo = input("Mais contas? (s/n): ")
    if denovo.lower() != "s":
        break