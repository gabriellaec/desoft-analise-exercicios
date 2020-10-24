def quantos_uns(x):
    i=0
    cont = 0
    x = str(x)
    while i < len(x):
        if x[i] == '1':
            cont +=1
            i+=1
		else: 
			i+=1
	return cont 