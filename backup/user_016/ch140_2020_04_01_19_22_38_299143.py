def faixa_notas(lista1):
    i = 0
    lista2 = []
    lista3 = []
    lista4 = []
    while i < len(lista1):
        if lista1[i] < 5:
            lista2.append(1)
        elif 5 <= lista1[i] <= 7:
            lista3.append(1)
        elif lista1[i] > 7:
            lista4.append(1)
        i +=1
    lista_final = [sum(lista2),sum(lista3),sum(lista4)]
    return lista_final