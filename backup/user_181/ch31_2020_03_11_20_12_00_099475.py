def eh_primo(n):
    cont = 1
    if n==0:
        return False
    elif n==1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    while cont<n:
        cont+=2
        if n%cont==0:
            return False
    else:
        return True
print(eh_primo(9))