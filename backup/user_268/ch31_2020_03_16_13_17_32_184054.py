def eh_primo(x):
    if x>2 and x%2==0:
        return False
    elif x==1 or x==0:
        return False
    c=3
    while c>x:
        if x%c==0:
            return False
        c+=2
    else:
        return True
print(eh_primo(10474753))