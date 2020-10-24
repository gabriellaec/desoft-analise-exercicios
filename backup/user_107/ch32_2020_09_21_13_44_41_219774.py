def lista_primos (n):
    count = 0
    num = 2
    while count < n:
        if eh_primo(num):
            print(num)
            count += 1
        num += 1
