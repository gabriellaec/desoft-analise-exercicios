def eh_crescente (x):
    x=[]
    i=0
    j=0
    while i < len(x):
		if x[i]>x[j] or j==0:
            x[j]=x[i]
			i+=1
        else:
            return false
return true        
        
            