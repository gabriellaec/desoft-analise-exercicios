def eh_primo (n):
    if n==2:
        return True
    if n==0 or n==1:
        return False
    i=3
    while  i<n:
        if n % i == 0:
        	return False 
        i = i+2
    return True 
