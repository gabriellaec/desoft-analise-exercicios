def nome_usuario(email):
	for e in len(email):
        if email[e] == '@':
            return email[ : e]
