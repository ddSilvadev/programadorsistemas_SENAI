#Revisão da prova no dia 31/03/2026 do curso Programador de sistemas SENAI
#Dionata da Silva | dionata_ds@hotmail.com

# Questão 1 
print("Questão 1")

nome = "Carlos"
idade = 17
print(f"Olá, {nome}! Você tem {idade} anos.")

# Resposta : Olá, Carlos! Você tem 17 anos.



#-----------------------------------
print("___"*25) #prints ____ to divide the questions
print("Questão 2")

#Quantas vezes a palavra "Python" será impressa


for i in range(3):
    print(f"{i}. Python")

# Resposta : 3 vezes (0, 1, 2). Array começa/conta do 0


#-----------------------------------
print("___"*25)
print("Questão 3")

# Qual opção será printada?

nota = 6
if nota >=7:
    print("Aprovado")
elif nota >=5:
    print("Recuperação")
else:
    print("Reprovado")

# Resposta: Recuperação



#-----------------------------------
print("___"*25)
print("Questão 4")

# O que será impresso?

balaio = ["maçã", "banana", "uva", "goiaba"]
print(balaio[1])


# Resposta: banana

#-----------------------------------
print("___"*25)
print("Questão 5")

# O laço abaixo vai rodar quantas vezes?

contador = 0
while contador < 4:
    contador += 1
    print(contador)

# Resposta: 4

#-----------------------------------
print("___"*25)
print("Questão 6")

# Complete para que o programa leia o nome digitado pelo usuário:
# nome = ?("Digite seu nome: ")

#nome = input("Digite seu nome: ")


# A resposta é input. Input é a função usada quando é preciso adquirir informações do usuário

#-----------------------------------
print("___"*25)
print("Questão 7")

# Complete para adicionar "laranja" à lista:

#balaio = ["maça", "banana"]
#balaio.?("jaca")

sacola = ["maça", "banana"]
sacola.append("jaca")
print(sacola)

# Resposta: O method append é usado para modificar/adicionar items a lista/array


#-----------------------------------
print("___"*25)
print("Questão 8")


produto = "caneta"
preco = 2.5
#print(
# Complete a f-string para exibir: "Produto: caneta, Preço: R$2.50"

#Resposta:
print(f"Produto: {produto}, Preço: R${preco}")

#-----------------------------------
print("___"*25)
print("Questão 9")

# Complete o for para percorrer a lista

cores = ["azul", "verde", "vermelho"]
#for cor ?
# Resposta: in cores
for cor in cores:
    print(cor)

#-----------------------------------
print("___"*25)
print("Questão 10")

# Complete para que o bloco execute quando a condição for falsa

idade = 16
if idade >= 18:
    print("Maior de idade")
# Resposta: operador else
else:
    print("Menor de idade")