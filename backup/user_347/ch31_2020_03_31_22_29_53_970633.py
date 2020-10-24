def eh_primo(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    if x%2==0:
        return False
    
    cont = 3
    while cont < x:
        if x% cont == 0:
            return False
        else:
            cont = cont + 2
    return True