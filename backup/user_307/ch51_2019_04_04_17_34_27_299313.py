def estritamente_crescente(lista):
	new=[]
	i=1
	new.append(lista[0])
	while i<len(lista):
		if lista[i]>new[len(new)-1]:
			new.append(lista[i])
		i+=1
	return new
print (estritamente_crescente(lista))