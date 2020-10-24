def quantos_uns(numero):
    n = str(numero)
    uns = 0
    i = 0
    while i <= len(n):
        a = n[i]
        if a == 1:
            uns +=1
        i += 1
        
    return uns