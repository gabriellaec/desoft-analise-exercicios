def zera_negativos(a):
    i = 0
    b = len(a)
    while i < b:
		if a[i] < 0:
            a[i] = 0
		i+=1
return a