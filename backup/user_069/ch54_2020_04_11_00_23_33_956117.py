def calcula_fibonacci (n):
    fibonacci=[1]*n
    i = 1
    while i < len(fibonacci)-1:
        fibonacci[i+1] = fibonacci[i] + fibonacci[i-1]
        i += 1
    return fibonacci