def eh_primo(x):
    if x < 2:
        return "nao primo"
    if x == 2:
        return "primo"
    elif x % 2 == 0:
        return "nao primo"
    elif x % 2 !=0:
        i = 3
        while i < x:
            if x % i != 0:
                i = i + 2
            elif x % i == 0: 
                return "nao primo"
        return "primo"
        
        
            
            
        