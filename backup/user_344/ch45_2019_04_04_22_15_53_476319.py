def zera_negativos(v):
	i=0
	while i<len(v):
    	if v[i]<0:
            v[i]=0
        i+=1
    return v
