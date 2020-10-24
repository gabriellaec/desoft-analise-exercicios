def verifica_numero (n):
	i = 0
    if n > 1:
   		 while len(n) >= i:
      		if  n == n[i]**n[i]:
       	        i += 1
                return True
        	else:
                return False