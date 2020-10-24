def quantos_uns(numero):
    i=0
    contador=0
    while i<len(numero):
        if str(numero)[i]=="1":
        	contador+=1
       	i+=1
	return contador