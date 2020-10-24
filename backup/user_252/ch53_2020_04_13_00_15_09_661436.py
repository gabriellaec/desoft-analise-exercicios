def soma_impares(lista):
    b=0
    c=0
    soma=[]
    for i in range(len(lista)):
        y=lista[i]
        if y%2!=0:
            soma.append(y)
        i+=1
    for b in range(len(soma)):
        x=soma[b]
        c+=x
    return c
    