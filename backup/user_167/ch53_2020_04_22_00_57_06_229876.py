def soma_impares (l):
    i=0
    soma=0
    while i < len(l):
        if l[i] % 2 != 0:
            soma+=l[i]
        i+=1
    return soma

    