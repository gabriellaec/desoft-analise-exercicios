def acha_bigrama(palavra):
    i=0
    lista=[]
    while i<len(palavra)-1:
        bigrama=palvra[i]+palavra[i+1]
        lista.append(bigrama)
		i+=1
	return lista