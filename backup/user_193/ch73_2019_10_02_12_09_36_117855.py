def remove_vogais(st):
	vogais = ["a","e","i","o","u",]
	i=0
	while i<len(st):
		if st in vogais:
			st.remove(i)
		i+=1