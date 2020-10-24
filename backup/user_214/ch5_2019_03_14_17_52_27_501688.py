def maior_primo(p):
    while p >= 2:
        i = p - 1
        p % 1 == 0
        return p


def éPrimo(n):
    i = 2
    é_primo = 0
    while i < n:
        if n % i ==0:
            break
        else:
            i = i+1
    if i == n:
        é_primo = False
        return False
    else:
        é_primo = True
        return True