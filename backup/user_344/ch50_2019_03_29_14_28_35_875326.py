def numero_no_indice(l):
    lista=[]
    i=0
    while i<len(l):
        if l[i]==i:
             lista.append(l[i])
        i+=1
    return lista
        
