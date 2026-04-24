# Execicio para se familiar com os operadores if, elif e else e seu uso.
# Também uma palhinha e introdução em importação e uso de bibliotecas


import math

peso = float(input("Peso em kg: "))
altura = float(input("Altura em metros: "))

imc = peso / (altura ** 2)
imc_arredondado = round (imc, 2)

print(f"\nSeu IMC é: {imc_arredondado}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obeso kkkkkk")