def conta_bigramas(string):
    bigrama=[]
    dicionario={}
    i=0
    while i<len(string)-1:
        x=string[i]+string[i+1]
        bigrama.append(x)
        i+=1
	n=bigrama.count(bigrama[i])
	dicionario[bigrama[i]]= n
	
	return dicionario