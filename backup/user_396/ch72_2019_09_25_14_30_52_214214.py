def lista_caracteres(x):
    lis = []
    i = 0
    while i < len(x):
        if x[i] not in lis:
	        lis.append(x[i])
        i += 1
    return lis