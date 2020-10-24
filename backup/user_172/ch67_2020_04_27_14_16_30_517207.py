def alunos_impares(lista):
    lista2 = []
    for i in lista:
        if i%2 != 0:
            lista2.append(lista[i])
    print(lista2)
    return lista2