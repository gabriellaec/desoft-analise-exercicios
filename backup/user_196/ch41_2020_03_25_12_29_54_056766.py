def zera_negativos(a):
	i = 0
	while i < len(a):
		if a[i] < 0:
			a[i] = 0
		i += 1
	return a