def eh_primo(n):
    if (n != 0) and (n != 1):
        i = n
        while i>0:
            func = n % 2
            func2 = n % i
            i -= 2
            if (func == 0) or (func2 == 0):
                return False
            else:
                return True
            
            