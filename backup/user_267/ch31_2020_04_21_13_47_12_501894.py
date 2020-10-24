def eh_primo(n):
    if (n != 0) and (n != 1):
        for i in range(n, 0, -2):
            func = n % 2
            func2 = n % i
            if (func == 0) or (func2 == 0):
                return False
            else:
                return True
            
            