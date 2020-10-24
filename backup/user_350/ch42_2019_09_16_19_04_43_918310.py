def quantos_uns(n):
    uns =0
    i=0
    n=str(n)
    while i < len(n):
        if n[i] == str(1):
            i+=1
            uns+=1
        else:
            i+=1
	return uns
    