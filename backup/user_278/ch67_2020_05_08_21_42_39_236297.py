def alunos_impares (lista):
    lista_im = []
    i = 0
    while i < len (lista):
        if i % 2 == 0:
            continue
        else:
            lista_im.append(lista[i])
    return lista_im