def quantos_uns(n):
    s = 0
    i = 0
    x = list(n)
    while i < len(x):
    	if n[i] == 1:
        	s += 1
    return s     
