def eh_primo(x):
    if x <= 1: 
        return False
    if x == 2: 
        return True
    if x%2==0:
        return False

    tmp = 3
    while tmp < x: 
        if x%tmp==0:
            return False
        else:
            tmp = tmp + 2
  
    return True

def maior_primo_menor_que(x):
    while x>1:
        if eh_primo(x):
            return x
        else:
            x = x - 1
    return -1
