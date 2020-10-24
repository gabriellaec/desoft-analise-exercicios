def interseccao_valores(di1,di2):
    d1=di1.values()
    d2=di2.values()
    lista=[]
    for valor1 in di1:
        for valor2 in d2:
            if valor1==valor2:    
                lista.append(valor1)
    return lista