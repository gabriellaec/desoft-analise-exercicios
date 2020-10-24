def remove_vogais(st):
	vogais = ["a","e","i","o","u",]
	i=0
	for i in vogais:
		if i in st:
			st.remove(i)
		i+=1