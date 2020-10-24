def alunos_impares(lista):
    lista2 = []
    contador = 0
    while contador < len(lista):
        if contador % 2 == 1:
            lista2.append(lista[contador])
        contador = contador + 1
    return lista2