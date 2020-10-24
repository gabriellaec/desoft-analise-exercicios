def estritamente_crescente(Lista_Numero):
	Lista_Nova_Cresc = []
	for i in range(len(Lista_Numero)-1):
		if (Lista_Numero[i]<Lista_Numero[i+1] and Lista_Numero[i] not in Lista_Nova_Cresc) or (Lista_Numero[i]==Lista_Numero[i+1] and Lista_Numero[i-1]<Lista_Numero[i] and Lista_Numero[i] not in Lista_Nova_Cresc):
			Lista_Nova_Cresc.append(Lista_Numero[i])
	return Lista_Nova_Cresc