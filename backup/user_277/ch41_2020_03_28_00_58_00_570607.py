def zera_negativos(a):
    i=0
    while i>len(a):
        i+=1
        if a[i]>=0:
            a[i]=a[i]
        else:
            a[i]=0
	return a[0]