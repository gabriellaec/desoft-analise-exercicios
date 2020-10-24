def junta_listas(lista):
    lista_p=[]
    for i in lista:
        for j in i:
            lista_p.append(j)
    return lista_p
lista=[[1, 2, 3], [4, 5, 6], [7, 8], [9], [10]]
q=junta_listas(lista)
print(q)