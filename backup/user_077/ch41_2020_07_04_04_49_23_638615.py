def zera_negativos(x):
    lista_final=[]
    for valor in x:
        if valor<0:
            valor=0
            lista_final.append(valor)
        else:
            lista_final.append(valor)
    return (lista_final)     