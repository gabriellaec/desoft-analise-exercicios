def eh_primo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        if n%2 == 0:
            return False
        else:
            impar = 3
            while impar < n:
                if n%impar == 0:
                    return False
                impar = impar + 2
            return True
        
        
def lista_primos(n):
    l=[]
    primos=0
    while len(l)<n:
        while eh_primo(primos)==False:
        	primos+=1
        l.append(primos)
        primos+=1
    return l
        
        
        
    
    