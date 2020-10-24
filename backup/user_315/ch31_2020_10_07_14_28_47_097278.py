def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    elif n>1:
        if n%2==0:
            return False
        else:
            y=3
            h=True
            while h:
                if y<n and n%y==0:
                    return False
                elif n==y:
                    return True
                    h=False 
                y+=2
                
                