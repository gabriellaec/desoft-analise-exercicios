def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        if n%2==0:
            return False
        else:
            d=3
            while n>d:
            	if n%d==0:
                	return False
            	else:
                	d+=2
        	return True
                
                
            
        