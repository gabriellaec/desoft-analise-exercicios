def eh_crescente(lista):
    crescente=True
    for e in range(1,len(lista)):
        if lista[e]<lista[e-1]:
            return False
    else:
    	return crescente


        