def estritamente_crescente(n):
    lis=[]
    i=1
    lis.append(n[0])
    while i < len(n):
    	if n[i]>lis[0]:
    		lis.append(n[i])
    	i+=1
    return lis
    
   