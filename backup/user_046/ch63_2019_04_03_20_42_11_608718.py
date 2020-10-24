def pos_arroba(email):
 pos=-1
 i=0
 n=len(email)
	while i<n:
		if email[i]=='@':
			pos=i
		i+=1
	
    return pos
