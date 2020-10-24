def lista_primos(n):
    lista[0]*n
    e=2
    d=3
    x=0
    while n>0:
        lista[x]=e
        e+=1
        x+=1
		while e%2==0 or (e%d==0 and e>d):
			d=3
			e+=1
			while e%d!=0:
				d+=2
    return lista