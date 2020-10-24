def alunos_impares(lista):
    a=[]
    i = 0
    while i < len(lista)-1:
        a.append(lista[i+1])
        i += 2
    return a