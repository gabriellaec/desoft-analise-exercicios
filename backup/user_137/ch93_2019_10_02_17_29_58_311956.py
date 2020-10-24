import math

def verifica_numero(n):
    if n < 1:
        return False
    else:
        number = list(str(n))
        r = 0
        for i in range(len(number)):
            r += math.pow(int(number[i]), int(number[i]))
        if r == n:
            return True
        else:
            return False