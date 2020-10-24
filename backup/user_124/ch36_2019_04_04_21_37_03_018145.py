def eh_primo(n):
    if n >= 2:
    	conta = 2
    	while conta < n:
        	if n % 2 == 0 or n % conta == 0:
            	return False
        	conta += 1
    	return True