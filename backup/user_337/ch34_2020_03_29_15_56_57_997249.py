def eh_primo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        if n%2 == 0:
            return False
        else:
            impar = 3
            while impar < n:
                if n%impar == 0:
                    return False
                impar = impar + 2
            return True
        
def maior_primo_menor_que (n):
    if n<2:
        return -1
    else:
        while eh_primo(n) == False:
            n = n-1
        return n