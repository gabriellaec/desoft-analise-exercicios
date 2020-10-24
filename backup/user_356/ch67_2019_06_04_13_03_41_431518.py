def alunos_impares(lista):
    lista_impar=[]
    n=len(lista)
    for i in range(1, n, 2):
        lista_impar.append(lista[i])
    return lista_impar