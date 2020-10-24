def classifica_lista(lista):
    n = len(lista)
    i = 1 
    while i < n:
        if lista[i-1] < lista[i]:
            i += 1
            print('crescente')
        elif lista[i-1] > lista[i]:
            i += 1
            print('decrescente')
        else:
            print('nenhum')