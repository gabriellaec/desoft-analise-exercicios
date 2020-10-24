def eh_primo(n):
    x=n
    i=3
    if x%2==0 and x!=2:
        return False
    elif x<2:
        return False
    elif x==2:
        return True
    else:
        if x%i==0 and x!=3:
            return False
        elif x==3:
            return True
        elif x%i!=0:
            while x>=i:                
                i+=2
                if x%i==0:
                    return False
                elif x%i!=0:
                    return True