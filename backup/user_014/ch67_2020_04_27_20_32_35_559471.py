def alunos_impares(lista_nomes):
    lista_impares = []
    i = 0
    while i < len(lista_nomes):
        impar = lista_nomes[i::2]
        lista_impares.append(impar)
        i +=1
    return lista_impares