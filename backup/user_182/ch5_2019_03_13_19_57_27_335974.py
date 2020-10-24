def ehprimo(k):
    p=True
    c=2
    while c<k:
        if k%c==0:
            return False
        c+=1
    return p

def maior_primo_menor_que(n):
    c=n
    while c>=2:
        if ehprimo(c):
        	return c
    	c-=1
    return -1
