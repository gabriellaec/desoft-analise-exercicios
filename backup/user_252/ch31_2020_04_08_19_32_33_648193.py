def eh_primo(x):
    if x==1 or x==0:
        return False
    elif x==2:
        return True
    elif x>1:
        if x%2==0:
            return False 
        else:
            y=3
            invalid=True 
            while invalid:
                if y<x and x%y==0:
                    return False
                elif y==x:
                    return True
                    invalid=False
                y+=2
                