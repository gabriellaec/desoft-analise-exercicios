
def maior_primo_menor_que(n):
    i = n
    while i>0:
		if n%i==0:
            i-=1
        elif n%i!==0:
            return n
        n -= 1
    