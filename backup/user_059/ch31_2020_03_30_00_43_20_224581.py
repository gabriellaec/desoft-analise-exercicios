def eh_primo(x):
    if x==0 or x==1:
       return False
    elif x==2:
        return True
    else:
        if x%2==0: 
            return False
        else:
            i = 3
            while i<x:
                if x%i == 0:
                    break
                    i+=1
            if i==0:
                return True
            else:
                return False