def numero_no_indice(lista):
    x = 0
    a = []
    for i in lista:
        if i == lista[x]:
            a.append(i)
        x+=1
    return a