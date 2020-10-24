def eh_crescente(x):
    i = 1
    while i < len(x) + 1:
        if x[i] > x[i-1]:
        	return True
        i += 1
        else: 
            return False
        