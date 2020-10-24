def conta_a(palavra):
    i = 0
    s = 0
    while i <= len(palavra):
        if palavra[i] == 'a':
            s += 1
        i+=1
	return(s)