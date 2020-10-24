def verifica_primo(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for r in range(2, n):
            if n%r == 0:
                return False
    return True
  
def maior_primo_menor_que(n):
    if n<2:
        return -1
    while n > 1:
        if verifica_primo(n):
            return n
        n -= 1;
