def eh_crescente(l):
    i = 0
    while i < len(l):
        if l[i] < l[i+1]:
            return True
        else:
            return False
    	i+=1        