def eh_crescente (x):
    x=[]
    i=0
    while i < len(x):
		if x[i]>x[j]:
            x[j]=x[i]
			i+=1
        else:
            return False
    return True        
        
            