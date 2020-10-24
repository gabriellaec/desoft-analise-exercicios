def alunos_impares(lista):
    lista1=[]
    i=0
    while i<len(lista):
        lista1.append(lista[i+1])
        i+=1
    return lista1