def pos_arroba(email):
	contador=0
	for i in email:
		if i=='@':
			return contador+1
	contador+=1