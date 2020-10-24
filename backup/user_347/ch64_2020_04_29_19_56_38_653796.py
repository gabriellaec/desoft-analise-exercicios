def acha_bigramas(x):
    lista=[]
    i=0
    while i<len(x):
        z = x[i:i+2]
        if z not in lista:
            lista.append(z)
        i+=1
        if len(lista[-1])<2:
            lista.pop()
        
    return lista