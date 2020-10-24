def verifica_progressao(lista):
    
	i = 0
	PA = True
	PG = True 
	AG = True
	while i < len(lista) - 2:
    	if not lista[i + 1] - lista[i] == lista[2+i] - lista[i+1]:
        	PA = False
            return "PA"
        elif not lista[i+1]/lista[i] == lista[2+i]/lista[1+i]:
            PG = False
            return "PG"
        elif not lista[i + 1] - lista[i] == lista[2+i] - lista[i+1] and lista[i+1]/lista[i] == lista[2+i]/lista[1+i]:
            AG = False
            return "AG"
        else: 
            return "NA"
         