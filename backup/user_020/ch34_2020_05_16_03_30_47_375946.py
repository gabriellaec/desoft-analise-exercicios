def eh_primo(n):
    impar = 3
    if n <= 1:
        return False
    if n%2 == 0:
        if n == 2:
            return True
        else: 
            return False
    else:
        while impar < n:
            if n % impar == 0:
                 return False
            else:
                impar += 2
        return True
def maior_primo_menor_que(n):
    if eh_primo == False:
        return -1
    else:
        x = 0
        while x <= n:
            x += 1
            if x == n and eh_primo(x) == True:
                return x
            elif x == n and eh_primo(x) == False:
                x = x - 1
                return x
print maior_primo_menor_que(11)