def eh_crescente(n):
    i=1
    crescente=True
    while i<len(n):
        if n[i-1]>=n[i]:
        	return False
        i+=1
    return True