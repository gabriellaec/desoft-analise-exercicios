def pos_arroba(email):
    i=0
    contador = 0
    for i in email:
        if i == '@':
            return contador + 1
        else:
            i += 1
            contador += 1
	return contador
      