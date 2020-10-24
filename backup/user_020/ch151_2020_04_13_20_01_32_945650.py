def classifica_lista(lista):
    i = 0
    if len(lista) < 2:
        print('nenhum')
    for i in range(i, len(lista)):
        if lista[i] < lista[i+1]:
            print('crescente')
        elif lista[i] > lista[i+1]:
            print('decrescente')
        elif lista == []:
            print('nenhum')
        else:
            print('nenhum')
    