def remove_vogais(string):
	lista1 = []
	for i in string:
		lista1.append(i)

	for ch in lista1:
		if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
			lista1.remove(ch)
	return lista1
	




       