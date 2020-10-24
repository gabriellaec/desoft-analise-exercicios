def estritamente_crescente(lista):
    cresc=[]
    i=1
    while i<len(lista):
        if lista[0]<lista[i]:
            cresc.append(lista[i])
        i+=1
	return cresc
    