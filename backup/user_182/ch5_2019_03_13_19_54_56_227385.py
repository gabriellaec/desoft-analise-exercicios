def éprimo(k):
    p=True
    c=2
    while c<=(k-1):
        if k%c==0:
            return False
        c+=1
    return p

def maior_primo_menor_que(n):
    c=n
    while c>=2:
        if éprimo(c):
        	return c
    	c-=1
    return -1
