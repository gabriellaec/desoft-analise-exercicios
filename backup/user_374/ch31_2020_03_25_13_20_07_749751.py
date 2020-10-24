def eh_primo(x):
    k = 2
    teste = True
    if x <= 1:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
   	
    while teste:
        if x%k == 0:
            return False
        else:
            k += 1
    return True
            