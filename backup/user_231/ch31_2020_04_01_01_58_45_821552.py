def eh_primo(n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    r= n%2
    if r != 0:
        d=1
        while d<n:
            d +=2
            if n==d:
                return True
            if n%d !=0:
                if d>=n:
                    return True
            else:
                return True
    else:
        return False
            
           
            
        