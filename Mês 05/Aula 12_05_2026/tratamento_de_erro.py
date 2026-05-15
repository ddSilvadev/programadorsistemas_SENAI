# Exercicio para tratamento de erro

try:
    numero = int(input("Digite um numero inteiro: "))
    resultado = 100 / numero

    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("\nErro: não é possivel dividir por 0")