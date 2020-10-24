def verifica_lista(lista):
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