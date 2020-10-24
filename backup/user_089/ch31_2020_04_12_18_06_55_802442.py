def eh_primo(x):
    i = 1
    if x == 0 or 1:
        return ("False")
    while i < x and x > 1:
        if x%2 == 0:
            if x/2 == 1:
                return ("True")
            if x/2 != 1:
                return ("False")
        if x%2 != 0:
            if x%i == 0:
                if x/i == 1:
                    return ("True")
                if x/i != 1:
                    return ("False")
            else:
                i = i + 2
            
        
            