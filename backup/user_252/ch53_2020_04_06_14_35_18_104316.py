def soma_impares (soma):
    b=0
    c=0
    lista=[]
    for i in range(len(soma)):
        y=soma[i]
        if y%2=0:
            lista.append(y)
    for b in range(len(lista)):
        x=lista[b]
        c+=x
    return c
    