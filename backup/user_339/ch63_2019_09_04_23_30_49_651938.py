def pos_arroba(email):
    i = 0
    x = list(email)
    l = len(x)
    while i < l:
    	if x[i] == '@':
        a = i + 1
        return a