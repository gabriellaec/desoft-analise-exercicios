def verifica_lista(lista):
    lista1=[]
    if lista==lista1:
        return 'misturado'
    lista2=[]
    lista3=[]
    for j in lista:
        if j % 2 == 0:
            lista2.append(j)
        else:
            lista3.append(j)
    if lista2==lista:
        return 'par'
    elif lista3==lista:
        return 'ímpar'
    else:
        return 'misturado'