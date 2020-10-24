def numero_no_indice(lista):
    i=0
    igual=[]
    while i < len(lista):
        if lista[i] == i:
            igual.append(lista[i])
		i+=1
	return igual