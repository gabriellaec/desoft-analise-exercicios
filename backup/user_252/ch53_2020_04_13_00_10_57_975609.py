def soma_impares(lista):
    i=0
    b=0
    c=0
    soma=[]
    while i<len(lista):
        y=lista[i]
        if y%2!=0:
            soma.append(y)
        i+=1
    while b<len(soma):
        x=soma[b]
        c+=x
        b+=1
    return c
    