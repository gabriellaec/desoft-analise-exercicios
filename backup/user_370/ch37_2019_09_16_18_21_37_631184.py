def lista_primo(n):
    if n==0:
        return False 
    elif n==1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        y=n-2
        while y>2:
            if n%y==0:
                return False 
            y=y-2
        return True  
    while
    
 