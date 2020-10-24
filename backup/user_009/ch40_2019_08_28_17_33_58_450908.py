def fatorial(x):
	a = 1 
	n = 1 
	x = int(input('num:'))
	while a <= x:
		a = a*n
		a += 1 
	return fatorial(x)