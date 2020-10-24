n = int()
def maior_primo_menor_que(n):
    x = 3
    if n % 2 == 0 and n != 2 or n == 0 or n == 1:
        primo = False
    while n > x:
        if n % x == 0:
            primo = False
        x += 2
    else:
        primo = True
    if primo == True:
        return n
    if primo == False:
        if n < 2:
            return -1
    else:
        lista = [2]
        n_primo = 3
        while lista[-1] < n:
            for i in range(2, n_primo):
                if n_primo % i == 0:
                    break
                if i == (n_primo - 1):
                    lista.append(n_primo)
            n_primo += 1
            return lista[-1]