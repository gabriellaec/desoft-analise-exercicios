def calcula_fibonacci (n):
    fibonacci=[1]*n
    i = 2
    while i < len(fibonacci)-1:
        fibonacci[i+1] = fibonacci[1] + fibonacci[i-1]
        i += 1
    return fibonacci