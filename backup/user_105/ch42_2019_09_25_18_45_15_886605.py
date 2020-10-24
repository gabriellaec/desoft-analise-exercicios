def quantos_uns(x):
	uns = [] 
	x = str(x)
	for i in x:
        
		if i == '1':
			uns.append(i)
	return len(uns)
