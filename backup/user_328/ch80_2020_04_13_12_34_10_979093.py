def interseccao_chaves(lista1,lista2):
    lista = []
    for k in lista1:
        lista.append(k)
    listanova = []
    cont = 0 
    for i in lista2:
        if i == lista[cont]:
            listanova.append(i)
            cont += 1
        else:
            cont += 1
    return listanova