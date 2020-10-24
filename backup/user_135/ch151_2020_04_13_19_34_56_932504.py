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
        d = 'decresceu'
        c = 'cresceu'
        lista_d = [d*(len(lista)-1)]
        lista_c = [c*(len(lista)-1)]

        if lista_de_verificacao == lista_c:
            return ('crescente')
        elif lista_de_verificacao == lista_d:
            return ('decrescente')
        else:
            return ('nenhum')