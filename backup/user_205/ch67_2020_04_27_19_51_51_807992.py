def alunos_impares(lista):
    opa=[]
    for i in range(len(lista)):
        if i == 0 or i%2==0:
            pass
        else: 
            opa.append(lista[i])
    return opa