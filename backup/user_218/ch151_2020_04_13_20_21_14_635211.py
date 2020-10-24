def classifica_lista(lista):
i = 0
while len(lista) >= 2:
    if lista[0] < lista[1]:
        print('crescente')
        i = i + 1
    elif lista[0] > lista[1]:
        print('decrescente')
        i = i + 1
    else:
        print('nenhum')