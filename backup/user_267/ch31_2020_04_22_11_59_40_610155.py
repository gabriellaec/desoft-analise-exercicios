def eh_primo(n):
    if (n == 0) or (n == 1):
        return False
    elif n == 2:
        return True
    else:
        i = n-1
        if n % 2 == 0:
            return True
        while i>0:
            if n % i == 0:
                return False
            i -= 2
            if i == 0:
                return True

            
            