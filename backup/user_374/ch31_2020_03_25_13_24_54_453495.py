def eh_primo(x):
    k = 3
    teste = True
    if x <= 1:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
   	
    while x < k :
        if x%k == 0:
            return False
        else:
            k += 2
    return False
            