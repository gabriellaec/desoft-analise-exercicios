def classifica_lista(lista):
while len(lista) >= 2:
    i = 0
    if lista[0] < lista[1]:
        print('crescente')
        i = i + 1
    elif lista[0] > lista[1]:
        print('decrescente')
        i = i + 1
    else:
        print('nenhum')