def pos_arroba(email):
    i=0
    while i < len(email):
		if email[i]=='@':
            resp= i
        i+=1
        return resp