def alunos_impares(lista):
    lista2 = []
    i = 0
    while i < len(lista):
        if i % 2 == 0:
            lista2.append(lista[i])
        i +=1
    return lista2