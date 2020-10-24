def se_y_é_primo(y):
    if y<=1:
        return False
    elif y==2:
        return True
    elif y==3:
        return True
    elif y%2 == 0:
        return False
    elif y%3 == 0:
        return False
    elif y%1 == 0 and y%y ==0:
        return True
    else:
        return False
   

def maior_primo_menor_que(n):
    while y<=n:
        if se_y_é_primo(y) = True:
            return y
        else:
            return -1
    
    
    