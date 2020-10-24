def eh_primo(k):
    c=2
    if k == 2:
        return True
    elif k < 2:
        return False
    while c < k-1:
        if k%c == 0 :
            return False
        else:
            c += 1
            return True


def maior_primo_menor_que(n):
    n = int(n)
    if n < 2:
        return -1
    cont = n
    while eh_primo(cont) == False:
        cont = cont - 1
    return cont