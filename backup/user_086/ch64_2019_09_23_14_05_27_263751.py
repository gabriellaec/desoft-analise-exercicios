def pos_arroba(email):
	contador=0
	for i in email:
		if i=='@':
			return contador
		contador+=1
def nome_usuario(email):
    email[ :pos_arroba(email)]
    return 