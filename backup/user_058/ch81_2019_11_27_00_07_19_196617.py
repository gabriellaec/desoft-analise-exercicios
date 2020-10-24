def interseccao_valores(dicionario1,dicionario2):
    lista1 = []
    lista2 = []
    lista = []
    for i in dicionario1.values():
        lista1.append(i)
    for i in dicionario2.values():
        lista2.append(i)
   	for i in lista1:
        if i in lista2:
            lista.append(i)
    return lista