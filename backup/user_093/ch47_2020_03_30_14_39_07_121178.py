def estritamente_crescente(n):
    lis=[]
    i=1
    t=0
    lis.append(n[0])
    while i < len(n):
    	if n[i]>lis[t]:
    		lis.append(n[i])
    	i+=1
    return lista
    
   