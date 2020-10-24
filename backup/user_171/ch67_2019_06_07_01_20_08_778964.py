def alunos_impares(lista):
    impar=[]
    for i in range(len(lista)):
        if i %2!=0 and i!=0:
            impar.append(lista[i])     
    return impar
            