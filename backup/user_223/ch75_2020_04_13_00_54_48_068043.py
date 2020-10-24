def verifica_primos(lista):
	dic = {}
	for e in lista:
		el = int(e)
		if el==2 or (el!=2 and el%2!=0 and not -1<=el<=1):
			dic[e]=True
		elif (el!=2 and el%2==0) or (-1<=el<=1):
			dic[e]=False
	return dic