def asteriscos(n):
    lista=[]
    i=0
    soma=0
    while i<n:
        lista.append('*')
        soma+=lista[i]
        i+=1
    return soma
    