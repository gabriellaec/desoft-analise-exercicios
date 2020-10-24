def classifica_lista(lista):
i = 0
if len(lista) >= 2:
    while lista[0] < lista[1]:
        print('crescente')
        i = i+1
    while lista[0] > liata[1]:
        print('decrescente')
        i = i + 1
else:
    print('nenhum')