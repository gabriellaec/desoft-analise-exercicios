def filtra_positivos(n):
    i=0
    lista =[]
    while i<len(n):
        if n[i]>0:
            lista.append(n[i])
        i+=1
    return lista
        
        
        