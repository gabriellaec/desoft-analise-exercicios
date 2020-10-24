def maior_primo_menor_que(n):
    def eh_primo(x):
        if x == 2:
            return True
        elif x == 0 or x == 1:
            return False
        elif x % 2 == 0:
            return False
        else:
            i = 3
            while i < x:
                if x % i == 0:
                    return False
                    i = i + 2
            return True
    
    x = n
    if n > 0:
        while x <= n and x > 0:
            if eh_primo(x):
                return x
            x = x - 1  
    if n == 1:
        return -1     
    else:
        return -1