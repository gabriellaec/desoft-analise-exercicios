def maior_primo_menor_que(n):
    if n<0:
        return -1
    elif n<2:
        return False
    elif n==2:
        return True
    else:
        for r in range(2, n):
            if n%r == 0:
                return False
    return True