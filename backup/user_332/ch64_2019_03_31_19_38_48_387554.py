def pos_arroba(email):
    i = 0
    for e in email:
        if (e == "@"):
            return (i)
        else:
            i += 1
    return (i)

def nome_usuario (email):
	a = pos_arroba(email)
    return(email[:a])