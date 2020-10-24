def numero_no_indice(lista):
    resp=[]
    i=0
    while i<len(lista):
        if lista[i]==i:
            resp.append(lista[i])
	return resp
            