valor_global = "Global"

def minha_funcao():
    print("Minha função")
    valor_local = "Local"

minha_funcao()


print(valor_global) # normal, código todo pode ler
#print(valor_local) # erro, pois essa variavel só existe dentro da função
