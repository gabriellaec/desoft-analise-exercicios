def estritamente_crescente(n):
    i=0
    a=[0]*n
    while i<len(a):
        if a[i]>a[i+1]:
            del a[i+1]
        i+=1
	return a
        