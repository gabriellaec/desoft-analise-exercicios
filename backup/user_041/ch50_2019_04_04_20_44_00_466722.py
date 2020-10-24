def numero_no_indice(lista):
    i=0
    cont=[]
    while i<len(lista):
        if lista[i]==i:
            cont.append(lista[i])
     	i+=1
  	return cont