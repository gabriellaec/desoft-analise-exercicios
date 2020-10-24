def classifica_lista(lista):
    if len(lista) < 2:
        return ('nenhum')
    else:
        lista_de_verificacao = []
        for indice in range(len(lista)-1):
            if lista[indice] < lista[indice+1]:
                lista_de_verificacao.append('cresceu')
            elif lista[indice] > lista[indice+1]:
                lista_de_verificacao.append('decresceu')
        if lista_de_verificacao == list('cresceu'*(len(lista)-1)):
            return ('crescente')
        elif lista_de_verificacao == list('decresceu'*(len(lista)-1)):
            return ('decresceu')
        else:
            return ('nenhum')