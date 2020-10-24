
def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d < n:
            if n % d == 0:
                return False
            else:
                d += 1
        while d >= n:
            return True


def maior_primo_menor_que(m):
    while not eh_primo(m):  
        m -= 1
    return m
    
print(maior_primo_menor_que(1))