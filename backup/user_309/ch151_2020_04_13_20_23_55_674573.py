def classifica_lista(lista):
    if len(lista)  < 2:
        return 'nenhum'
    else:
        for i in range (len(lista)-1):
            if lista[i+1]>lista[i]:
                return 'crescente'
            if lista[i+1]<lista[i]:
                return 'decrescente'
            else:
                return 'nenhum'