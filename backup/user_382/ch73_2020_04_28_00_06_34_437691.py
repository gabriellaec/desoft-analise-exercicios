def remove_vogais(string):
	lista1 = []
	t = 0 
	for i in string:
		lista1.append(i)
	while t < len(string):
		for ch in lista1:
			if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
					lista1.remove(ch)
			t += 1	

	return lista1
