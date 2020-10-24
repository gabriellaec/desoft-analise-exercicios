Lista_Numero = [1,2,3,4,3,6,7,8,9,10]

def estritamente_crescente(Lista_Numero):
	Lista_Nova_Cresc = []
	i = 0
	for i in range(len(Lista_Numero)-1):
		if Lista_Numero[i]<Lista_Numero[i+1] and Lista_Numero[i] not in Lista_Nova_Cresc:
			Lista_Nova_Cresc.append(Lista_Numero[i])
	return Lista_Nova_Cresc
print(estritamente_crescente(Lista_Numero))