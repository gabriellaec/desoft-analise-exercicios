def verifica_primos(lista):
	dic = {}
	for e in lista:
		el = int(e)
		if (el!=2 and el%2==0) or (-1<=el<=1):
			dic[e]=False
		elif el==2 or (el!=2 and el%2!=0):
			dic[e]=True
	return dic