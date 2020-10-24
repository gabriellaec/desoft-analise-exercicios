def conta_bigramas(n):
    d={}
    for e in range (len(n)-1):
        bigramas=n[e:e+2]
        d[bigramas]=0
	for e in range (len(n)-1):
        bigramas=n[e:e+2]
        d[bigramas]+=1
	return d