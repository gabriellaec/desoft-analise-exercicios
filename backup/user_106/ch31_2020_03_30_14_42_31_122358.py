def eh_primo(n):
    elif (n+3)%2==0:
        return False
    else:
        i=3
        while i<(n+3):
            if n%i==0:
                return False
            i+=2
        return True