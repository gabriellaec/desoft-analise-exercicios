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