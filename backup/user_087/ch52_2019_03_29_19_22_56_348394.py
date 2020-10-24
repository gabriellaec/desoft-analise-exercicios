def eh_crescente(x):
    i = 1
    while i < len(x) + 1:
        i += 1
        if x[i] > x[i-1]:
        	return True
        else: 
            return False
        