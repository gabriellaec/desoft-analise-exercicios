def eh_primo(a):
    x=1
    if a == 2:
        return True
    elif a %2 == 0 or a%x == 0:
        x+=2
        return False
    else:
        return True