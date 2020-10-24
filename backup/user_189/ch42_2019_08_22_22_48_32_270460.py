def quantos_uns(num):
    uns=0
    for a in num:
        for b in a:
            if a[b]=="1":
                uns+=1
	return uns
                