def remove_vogais(st):
	vogais = ["a","e","i","o","u",]
    palavra=[]
	i=0
	for i in range (vogais):
		if i not in st:
			palavra.append(i)
    return palavra