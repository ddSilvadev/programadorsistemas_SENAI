"""
Calculadora com base na calc_avancada.py. Intuito dessa versão é implementar um fix para o problema da versão anterior só aceitar numero operador numero

Plano: entrada → token → processamento de operador → calcular
"""


# Resumo do que a função faz: recebe uma string como "3.5 + 2 * (10 - 4)" e quebra em uma lista de tokens — separando números dos operadores/símbolos:
# ["3.5 + 2 * (10 - 4)"]  →  [3.5, '+', 2.0, '*', '(', 10.0, '-', 4.0, ')']

def tokenize(entrada):
    tokens = []  # lista que vai guardar os tokens encontrados
    numero = ""  # acumula os dígitos de um número enquanto percorre a string

    i = 0
    while i < len(entrada):
        char = entrada[i]
        # verifica se os próximos 2 caracteres formam "**" ANTES do "*" simples, senão "**" seria lido como dois "*"
        if entrada[i:i+2] == "**":
            if numero:
                tokens.append(float(numero))
                numero = ""
            tokens.append("**")  # adiciona o operador de potência como token
            i += 2               # pula 2 posições para passar os dois caracteres "**"
            continue             # volta ao início do while sem executar o restante

        if char.isdigit() or char == ".":
            # caractere faz parte de um número (dígito ou ponto decimal)
            # acumula em 'numero' para montar o número completo
            # ex: '3', '.', '5' → acumula "3.5" antes de converter para float
            numero += char
        else:
            if numero:
                #converte para float e salva
                tokens.append(float(numero))
                numero = ""  # reseta o acumulador para o próximo número

            # adiciona o caractere atual se não for espaço
            if char.strip():
                tokens.append(char)

        i += 1  # avança para o próximo caractere

    # ao fim do loop pode restar um número acumulado
    # ex: "42" no final da string nunca encontra um char não-numérico para disparar o append
    if numero:
        tokens.append(float(numero))

    return tokens  # retorna a lista de tokens




def prioridade_alta(tokens):
    i = 0

    while i < len(tokens):
        if tokens[i] in ("*", "/", "**"):
            esquerda = tokens[i-1]
            op = tokens[i]
            direita = tokens[i+1]

            if op == "/" and direita == 0:
                return "Erro: divisão por zero"
            
            operacoes = {
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "**": lambda a, b: a ** b
            }

            resultado = operacoes[op](esquerda, direita)

            tokens[i-1:i+2] = [resultado]

            i -= 1
        else:
            i += 1

    return tokens

def prioridade_baixa(tokens):
    resultado = tokens[0]

    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = tokens[i+1]

        if op == "+":
            resultado += num
        elif op == "-":
            resultado -= num

        i += 2

    return resultado



def calcular(entrada):
    tokens = tokenize(entrada)
    tokens = prioridade_alta(tokens)

    if isinstance(tokens, str):
        return tokens

    return prioridade_baixa(tokens)


print(calcular("10+5*2"))      # 20
print(calcular("100-25/5"))    # 95
print(calcular("2**3+1"))      # 9