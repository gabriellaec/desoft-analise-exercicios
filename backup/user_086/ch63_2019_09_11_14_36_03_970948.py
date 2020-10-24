def pos_arroba(email):
	contador=0
	for i in email:
		print(i)
		if i=='@':
			return contador+1
		contador+=1