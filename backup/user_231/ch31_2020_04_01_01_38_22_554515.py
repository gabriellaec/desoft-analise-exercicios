def eh_primo(n):
    if n==0 or 1:
        return False
    if n==2:
        return True
    r= n%2
    elif r != 0:
        d=1
        while d<n and n%d !=0:
            d +=2
            if d>=n:
                return True
    else:
        return False
            
           
            
        