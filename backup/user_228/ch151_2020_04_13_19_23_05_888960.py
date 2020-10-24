def classifica_lista(lista):
    v=0
    f=100000000
    for i in lista:
        if i>v:
            v=i
            return 'crescente'
        elif i<v:
            v=i
            return 'decrescente'
        else:
            return 'nenhum'
           