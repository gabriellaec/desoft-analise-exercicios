def cresc(num):
	cresc = []
   	primeiro=num[0]
    cresc.append(primeiro)
    maior = primeiro
    
    for i in  range(1,len(num)):
        proximo = num[i]
		if proximo > maior:
            cresc.append(proximo)
            maior = proximo
	
    return cresc
    
  