def verifica_progressao(lista):
    i=1
    while i<len(lista):
    	deltaP[i].append(lista[i]-lista[i-1])
    	i+=1
    j=0
    PA=True
    while j<len(deltaP):
        if deltaP[j]==deltaP[j+1]:
            PA=False
        j+=1
    i=1
    while i<len(lista):
    	deltaP[i].append(lista[i]/lista[i-1])
    	i+=1
    j=0
    PG=True
    while j<len(deltaP):
        if deltaP[j]==deltaP[j+1]:
            PG=False
        j+=1
	if PA and PG:
        return "AG"
    elif PA:
        return "PA"
    elif PG:
        return "PG"
    else:
        return "NA"
  
