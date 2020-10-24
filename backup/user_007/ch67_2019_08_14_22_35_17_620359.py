def alunos_impares(lista = []):
    lista_aux = []
    for i in range(len(lista)):
        if i%2 == 1:
            lista_aux.append(lista[i])
    return lista_aux