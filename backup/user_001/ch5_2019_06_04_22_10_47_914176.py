def maior_primo_menor_que(n):
    if n<0:
        return -1
    elif n<2:
        return 0
    elif n==2:
        return 1
    else:
        for r in range(3, n):
            if n%r == 0:
                return 0
            
    return 1