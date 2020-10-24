def eh_primo(x):
    if x==1 or x==0:
        return False
    elif x==2:
        return True
    elif x%2==0:
        return False
    a=3

    while a<x:
        if x%a==0:
            return False
        a +=1
    return True

def maior_primo_menor_que(n):
    x=n
    while x>n:
        if eh_primo(x):
            return x
        x -= 1
    return -1