def eh_primo(n):
    x = 3
    if n % 2 == 0 and n != 2 or n == 0 or n == 1:
        return False
    while n > x:
        if n % x == 0:
            return False
        x += 2
    else:
        return True
eh_primo(n)

def maior_primo_menor_que(n):
    lista_primos = []
    if n == True:
        return n
    else:
        if n == False:
            for x in range(2,n):
                if n % x == 0:
                    break
                if x == (n - 1):
                    lista_primos.append(x)
            n += 1
maior_primo_menor_que(n)