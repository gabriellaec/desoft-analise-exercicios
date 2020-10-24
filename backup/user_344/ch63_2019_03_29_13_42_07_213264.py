def pos_arroba(email):
    contador=0
	while contador<len(email):
        if email[contador]== '@':
            return contador +1
        contador+=1
    