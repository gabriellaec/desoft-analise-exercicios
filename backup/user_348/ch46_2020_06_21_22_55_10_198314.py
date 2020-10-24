def numero_no_indice (lista):
    # Cria uma lista vazia onde serão adicionados os números
    resposta = []
    #Percorre a lista de entrada
    for i in range(len(lista)):
        # Verifica se o elemento é igual ao índice
        if i == lista[i]:
            #Adiciona o elemento à lista de resposta
            resposta.append(lista[i])
    return resposta