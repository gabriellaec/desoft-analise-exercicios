def eh_primo(x):
    i = 1 
    if x > 1:
        while i < x:
            if x%2 == 0:
                if x/2 == 1:
                    return ("True")
                else:
                    return ("False")
            if x%i == 0:
                if x/i == 1:
                    return ("True")
                else:
                    i = i + 1
                    return ("False")            
    else:
        return ("False")
        
            