def eh_primo(x):
    if x%2==0:
        return False
    elif x%2!=0:
        y=3
    if x%y==0:
        y+=2
        return False
    elif x==1 or x==0:
        return False 
    elif x==2:
        return True
    else:
        return True
def maior_primo_menor_que(n):
    global x
    while eh_primo:
        if n%x==0:
            return x
        else:
            return -1