def eh_primo(n):
    if (n == 0) or (n == 1):
        return False
    else:
        i = n
        while i>0:
            func = n % 2
            func2 = n % i
            i -= 2
            if (func == 0) or (func2 == 0):
                return False
            else:
                return True
            
            