def classifica_lista(lista):
    i = 1
    if len(lista) > 1:
        for i in range(len(lista)):
            if lista[i-1] < lista[i]:
                print('crescente')
            if lista[i-1 > lista[i]:
                print('decrescente')
            else:
                print('nenhum')
    else:
        print('nenhum')