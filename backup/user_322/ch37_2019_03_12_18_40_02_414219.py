def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 2 !=0:
        i = 3
        while i < n:
            if n % i != 0:
                i = i + 2
            elif n % i == 0: 
                return False
        return True
 
def imprime_primos(n):
    i = 0
    a = 0
    while a < n:
        if eh_primo(i) == True:
            print(i)
            a = a + 1
            i = i + 1
        else:
            i = i + 1