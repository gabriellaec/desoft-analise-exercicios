def quantos_uns(n):
	x =[int(i) for i in str(n)]
    contador = 0
    for e in x:
        if e == 1:
            contador+=1
    return contador