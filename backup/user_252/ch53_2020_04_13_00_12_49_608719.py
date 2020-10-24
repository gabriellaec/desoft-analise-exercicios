def soma_impares(lista):
    c=0
    soma=[]
    for i range(len(lista)):
        y=lista[i]
        if y%2!=0:
            soma.append(y)
        i+=1
    for b range(len(soma)):
        x=soma[b]
        c+=x
    return c
    