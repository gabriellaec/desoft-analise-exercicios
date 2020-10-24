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

def lista_primos(n):
    if n == 0:
        return []
    lista = [2]
    n_primo = 3
    while len(lista) < n:
        for x in range(2,n_primo):
            if n_primo % x == 0:
                break
            if x == (n_primo - 1):
                lista.append(n_primo)
        n_primo += 1
    return lista

def maior_primo_menor_que(n):
    lista = []
    if n == True:
        return n
    else:
        if n == False:
            lista_primos(n)
            return lista[-1]