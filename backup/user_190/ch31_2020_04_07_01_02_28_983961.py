def eh_primo(n):
    x=n
    i=3
    if x%2==0:
        return False
    elif x<=2:
        return True
    else:
        while x>i:
            if x%i==0:
                return False
            else:
                y=x/i
                i+=2
                if y==0:
                    return False
                else:
                    return True