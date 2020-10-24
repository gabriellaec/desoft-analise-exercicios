def quantos_uns(numero):
	a = str(numero)
	count=0
	for c in a:
		if c== '1':
			count+=1
	return count