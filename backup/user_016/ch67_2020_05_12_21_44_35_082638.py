def alunos_impares(lista):
    lista_final = []
    i = 0
    while i < len(lista):
        if i%2 != 0:
            lista_final.append(lista[i])
        i += 1
    return lista_final