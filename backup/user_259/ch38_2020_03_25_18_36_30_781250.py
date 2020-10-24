def quantos_uns(numero):
    numero = str(numero)
    i = 0
    uns = []
    while i<(len(numero)):
        if numero[i] == 1:
            uns.append(numero[i])
            i+=1
        else:
            i+=1
    return len(uns)
        
    