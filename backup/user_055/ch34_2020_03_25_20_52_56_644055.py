def maior_primo_menor_que(n):
    x = 3
    if n % 2 == 0 and n != 2 or n == 0 or n == 1:
        return False
    while n > x:
        if n % x == 0:
            return False
        x += 2
    else:
        return True
    lista = [2]
    n_primo = 3
    if eh_primo(n) == True:
        print (n)
    if eh_primo(n) == False:
        if n < 2:
            return -1
    else:
        while lista[-1] < n:
            for i in range(2, n_primo):
                if n_primo % i == 0:
                    break
                if i == (n_primo - 1):
                    lista.append(n_primo)
            n_primo += 1
            return lista[-1]