def inverte_lista(a):
    r=[]*len(a)
    i = 0
    n = len(a)
    while len(r) < len(a):
        r[i] = a[n]
        n = n - 1
        i = i + 1
	return r
    