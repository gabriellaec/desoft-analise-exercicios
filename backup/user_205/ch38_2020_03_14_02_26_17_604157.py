def quantos_uns(x):
    quantos_uns = 0
    contador = 0
    lista=[0]*1
    lista[0]=x
    while (x>contador):
        contador=+1
        if 1 in x:
            quantos_uns+=1
            return (quantos_uns)
        else:
            return (0)
            break
    
        