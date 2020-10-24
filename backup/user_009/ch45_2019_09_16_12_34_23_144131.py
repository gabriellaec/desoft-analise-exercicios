def zera_negativos(a)

    a = [2,5,4,-2,-6,10,59,-7,20]
    b = 0
    while b < len(a):
        if a[b] <= 0:
            a[b] = 0
        b+= 1
	return a