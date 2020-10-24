def estritamente_crescente(lista):
    if len(lista)==0:
        return []
    i = 0
    #Cria uma lista com o primeiro elemento da lista inicial
    resposta = [lista[0]]
    #Define a condição para o loop
    while i < len(lista):
        #Verifica se o próximo elemento da lista inicial é maior que o último elemento da lista resposta
        if lista[i] > resposta[len(resposta)-1]:
            #adiciona o elemento a lista resposta
            resposta.append(lista[i])
        i = i + 1
    return resposta