def alunos_impares(lista):
    lista2=[]
    for i in range(len(lista)):
        if i%2!=0:
            lista2.append(lista[i])
            
    return lista2