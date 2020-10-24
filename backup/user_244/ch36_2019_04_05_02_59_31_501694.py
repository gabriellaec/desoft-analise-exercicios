def primo(x):
    
    i = 2 
    if x == 2:
        return True
    elif x > 1:
        while i < x :
            if x%i == 0:
                return False
            
            i +=1
            return True
    else:
        return False
        
        
print(primo(4))