def primo(x):
    
    i = 2 
    
    while i < x:
        
        if x%i == 0:
            return False
        else:
            return True
        
        i += 1 
        
print(primo(9))