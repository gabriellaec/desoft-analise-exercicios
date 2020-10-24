def pos_arroba(string):
	contador = 0
	for i in string:
		if i == "@":
			break
		else:
			contador += 1
	return contador