def quantos_uns(numero):
    n=str(numero)
    soma=0
    i=0
    while i<len(n):
        if n[i] == 1:
            soma+=1
        i+=1
    return soma
        