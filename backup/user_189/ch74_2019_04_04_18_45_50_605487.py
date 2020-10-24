def conta_bigramas(palavra):
	i=0
	dic=dict()
	while(i<len(palavra)-1):
		bi=palavra[i]+palavra[i+1]
		if bi in dic:
			dic[bi]+=1
		else:
			dic[bi]=1
    	i+=1
	return dic
    
    	
    
             
