def alunos_impares(lista):
    i=0
    impar=[]
    while i<len(lista):
        if i%2!=0:
            impar.append(lista[i])
        i+=1
    return impar