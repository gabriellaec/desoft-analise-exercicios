def zera_negativos(a):
    num_elementos = len(a)
    i = 0
    while i<num_elementos:
        if a[i] < 0:
            a[i] = 0
        else:
            a[i] = a[i]
        i += 1
	print (a)