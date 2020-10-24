c=3
def eh_primo(x):
    x=float(input("type number"))
    if x>2 and x%2==0:
        return False
    elif x==1 or x==0:
        return False
    while c>x:
        if x%c==0:
            return False
        c+=2
    else:
        return True
    