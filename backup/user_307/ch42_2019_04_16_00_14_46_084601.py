def quantos_uns(n):
	h=str(n)
	i=0
	uns=0
	while i<len(h):
		if h[i]=='1':
			uns+=1
		i+=1
	return uns