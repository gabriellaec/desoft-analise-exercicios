def pos_arroba(email):
	contador=0
	for i in email:
		print(i)
		if i=='@':
			return contador
		contador+=1