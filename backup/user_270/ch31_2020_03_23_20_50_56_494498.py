
def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0 :
        return False
    else:
        t = 3
		k = True
        while k:
            if n % t == 0 and n == t:
                return True
            	k = False
            elif n % t == 0 and n != t:
                return False
                k = False
            else:
                t += 2
                
                
                
                
           
        
                