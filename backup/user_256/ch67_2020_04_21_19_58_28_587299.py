def alunos_impares(lista):
    i = 1
    nova=[]
    while i<len(lista):
        nova.append(lista[i])
        i+=2
    return nova