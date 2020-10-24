def eh_primo(num):
    i = 2 
    if num == 2:
        return True
    elif num == 0 or num == 1:
        return False
    while i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True
def maior_primo_menor_que(n):
    c = n
    while c <= n:
        if eh_primo(c):
            return c
        else:
            return -1
        c-=1
    return c
    