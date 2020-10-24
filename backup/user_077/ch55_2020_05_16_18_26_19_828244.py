def encontra_maximo(x):
    selecaofinal=[]
    for e in x:
        lista=x[:,e]
        i=1
        while i<len(lista):
            if lista[i]>lista[i-1]:
                n=lista[i]
            i+=1
        selecaofinal.append(n)
    h=0
    while h<len(selecaofinal):
        if selecaofinal[h]>selecaofinal[h-1]:
        m=selecaofinal[h]
        h+=1
    return m
        
        
            
                
                