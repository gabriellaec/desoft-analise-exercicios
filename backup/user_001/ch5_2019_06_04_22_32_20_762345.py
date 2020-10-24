def maior_primo_menor_que(n):
    if n<0:return -1
    if n<2:return False
    if n==2:return True
    for r in range(2, n):
    	if n%r == 0:return False    
    return True