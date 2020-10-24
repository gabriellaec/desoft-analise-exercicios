



def eh_primo(a):
    divisor = 2
    if a < 2:
        return False
    if a == 2:
        return True
    while a % divisor != 0 and divisor <= a/2:
        divisor +=1
    if a % divisor == 0:
        return False
    else:
        return True

def maior_primo_menor_que(b):
    if b == float:
        return -1
    if b < 0:
        return -1
    if eh_primo(b):
        return b
    else:
        i = b-1
        while i > 1:
            if eh_primo(i):
                return i
            else:
                i -= 1