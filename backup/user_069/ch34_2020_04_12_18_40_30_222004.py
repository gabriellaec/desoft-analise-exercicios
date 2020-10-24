def eh_primo (n):
    div = 3
    if n%2 == 0 and n != 2 or n == 1 or n == 0:
        return False
    
    while n > div:
        if n%div == 0:
            return False
        div += 1
    return True

def maior_primo_menor_que (n):
    if n <= 0 or n == 1:
        return -1
    i = n
    while i > 1:
        if eh_primo(i) == True:
            primo = i
        else:
            i -= 1
    return primo