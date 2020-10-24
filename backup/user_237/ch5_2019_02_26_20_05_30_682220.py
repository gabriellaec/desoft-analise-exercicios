def maior_primo_menor_que(n):
    a = False
    if n < 0:
    	return -1
    if primos(n) == True:
        return n
    else:
    	while a != True:
        	n -= 1
            a = primos(n)
       	return n 




def primos(x):
    Div =2
    
    while Div < x :
        
        if x % Div == 0:
            return False
        else:
            Div += 1
    return True
            