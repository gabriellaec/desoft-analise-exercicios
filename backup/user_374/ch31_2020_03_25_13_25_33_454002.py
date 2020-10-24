def eh_primo(x):
   
    teste = True
    if x <= 1:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
   	
    k = 3
    while x < k :
        if x%k == 0:
            return False
        else:
            k += 2
    return True            