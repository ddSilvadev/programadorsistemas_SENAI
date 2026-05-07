#funçoes nativas

def formatar_real(valor):
    # Passo 1: formatação padrao (EUA)
    texto = f"R$ {valor:,.2f}" # .2f > 2 casas decimais
    # 1234.5 > "R$ 1,234.50"

    # Passo 2: troca vírgula por marcador temporário
    texto = texto.replace(",", "X")
    # "R$ 1x234.50"

    # Passo 3: troca ponto por vírgula (decimal BR)
    texto = texto.replace(".", ",")
    # "R$ 1x234,50"

    # Passo 4: troca o X por ponto
    texto = texto.replace("X", ".")
    # "R$ 1.234,50"

    return texto


print(formatar_real(11111.50)) # R$ 11.111,50
print(formatar_real(6585630.50)) # R$ 6.585.630,50
print(formatar_real(122232421.50)) # R$ 122.232.421,50

preco = 1234.5
print(formatar_real(preco)) # R$ 1.234,50
