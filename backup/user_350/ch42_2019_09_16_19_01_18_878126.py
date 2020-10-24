def quantos_uns(n):
    uns =0
    i=0
    while i < len(n):
        if n[i] == 1:
            i+=1
        uns+=1
	return uns
    