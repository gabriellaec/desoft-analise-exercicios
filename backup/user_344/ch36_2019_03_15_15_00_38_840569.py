def eh_primo(num):
    contador= 2
	while contador<n:
        if num%contador==0:
            return False
    	if contador==2:
            contador+=1
        else:
            contador+=2
    return True 
        
        
