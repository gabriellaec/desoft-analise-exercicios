def encontra_maximo(x):
    lista1=x[0]
    lista2=x[1]
    lista3=x[2]
    i=1
    h=1
    while i<len(lista1):
        if lista1[i]>lista1[i-1]:
            a=lista1[i]
        if lista2[i]>lista2[i-1]:
            b=lista2[i]
        if lista3[i]>lista3[i-1]:
            c=lista3[i]
        i+=1
    selecaofinal=[a,b,c]
    while h<len(selecaofinal):
        if selecaofinal[h]>selecaofinal[h-1]:
            m=selecaofinal[h]
        h+=1
    return m
        
        
            
                
                