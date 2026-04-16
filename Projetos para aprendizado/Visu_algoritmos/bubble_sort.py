entrada = [5, 3, 1, 8] #entrada só está aqui para facilitar no desenvolvimento


def gerar_acoes(entrada): 
    acoes = []
    array_copia = entrada.copy()

    for passadas in range(len(array_copia) - 1): #define a quantidade de passadas necessarias (n-1)
        for i in range(len(array_copia) - passadas - 1):  #iterando no array de entrada: tamanho do array menos o numero de passadas menos 1
            acoes.append(("comparando", i, i+1))

            if array_copia[i] > array_copia[i+1]:  #se o numero atual (i) for menor que o numero á direita (i+1)
                acoes.append(("troca", i, i+1))
                array_copia[i], array_copia[i + 1] = array_copia[i + 1], array_copia[i] # reposicionando i, i+1 como i+1, i (a, b = b, a)

    return acoes





def reproduzir(entrada, acoes):
    array_copia = entrada.copy()
                        #           tipo       i  j
    for acao in acoes:  #acao = ("comparando", 0, 1)
        tipo, i, j = acao
        if tipo == "comparando":
            #print(array_copia)
            print(f"Comparando {array_copia[i]} e {array_copia[j]}...")
            #print(array_copia)
                

        elif tipo == "troca":
           print(f"Trocando {array_copia[i]} e {array_copia[j]} de posição!")
           array_copia[i], array_copia[j] = array_copia[j], array_copia[i]
           print(f"Sequência atual: \n {array_copia}")
        
    return array_copia

acoes = gerar_acoes(entrada)
print(reproduzir(entrada, acoes))