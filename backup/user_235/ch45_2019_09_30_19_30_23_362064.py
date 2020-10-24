lista_negativos=[]
def zera_negativos(x):
    y=0
    lista_negativos=[]
    while y < len(x):
        if x[y]<0:
            x[y]=0
        lista_negativos.append(x[y])
        y+=1
    return lista_negativos
        
