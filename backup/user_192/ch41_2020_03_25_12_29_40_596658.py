def zera_negativos(a):
    a_elementos = len(a)
    i = 0 
    while i < a_elementos:
        if i < 0:
            a[i] = 0
        i += 1
	return a 
    
    