def verifica_primos(lista):
	dic = {}
	for e in lista:
		if e==2 or (e!=2 and e%2!=0):
			dic[e]=True
		elif (e!=2 and e%2==0) or (neg(1)<=e<=1):
			dic[e]=False
	return dic