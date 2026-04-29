#função com Empacotador *args

def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(1, 2))
print(somar_tudo(45, 45, 2, 10))