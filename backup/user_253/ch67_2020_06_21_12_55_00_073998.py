def alunos_impares(lista):
    i=1
    b=[]
    p=0
    while i< len(lista):
        b.insert(p, lista[i])
        p+=1
        i+=2
    return b
        