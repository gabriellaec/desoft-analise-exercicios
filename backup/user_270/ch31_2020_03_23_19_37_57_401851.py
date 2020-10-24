t = 3
def eh_primo(n):
    if n % 2 == 0:
        return False
    else:
        while t < n :
            if n % t == 0 :
                return False
            else:
                t =+ 2
    return True
                