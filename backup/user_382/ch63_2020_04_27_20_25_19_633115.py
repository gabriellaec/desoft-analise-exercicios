def pos_arroba(n):
    for i in n:
        if i == '@':
            return n.index(i)

def nome_usuario (email):
	if '@' in email:
		user = email[:pos_arroba(email)]
		return user 
	else:
		return 0 