def eh_primo(n):
    x = 3
    if n % 2 == 0 and n != 2 or n == 0 or n == 1 or n < 0:
        return False
    while n > x:
        if n % x == 0:
            return False
        x += 2
    else:
        return True

def verifica_primos(lista_n):
    dict_primos = {}
    for n in lista_n:
        if eh_primo(n) == True:
            dict_primos[n] = True
        else:
            if eh_primo(n) == False:
                dict_primos[n] = False
    return dict_primos
