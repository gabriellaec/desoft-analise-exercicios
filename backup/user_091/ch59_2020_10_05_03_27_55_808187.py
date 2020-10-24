def asteriscos(n):
    lista=[]
    i=0
    soma=0
    while i<n:
        lista.append('*')
        i+=1
        soma+=lista[i]
        
    return soma
    