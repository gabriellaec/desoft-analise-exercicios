def numero_no_indice(n):
    lista=[]
    i=0
    while i<len(n):
        if i==n[i]:
            lista.append(i)
        i+=1
    return lista    
            