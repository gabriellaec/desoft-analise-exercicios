def eh_primo (x):
    if x == 1:
        return False
    if x % 2 == 0 and x!=2:
        return False

    i=3
    while i<x:
        if x%i==0:
            return False
        i += 2
    return True

print(eh_primo(7))

    
    

