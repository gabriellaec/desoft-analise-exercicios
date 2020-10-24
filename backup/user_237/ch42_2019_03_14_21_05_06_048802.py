def quantos_uns(n):
    contador = 0
    x =[int(i) for i in str(n)]
    for e in x:
        if e == 1:
            contador+=1
    return contador