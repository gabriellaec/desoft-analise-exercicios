def calcula_fibonacci (n):
    i = 0
    fibonacci = [0]*n
    fibonacci [0] = 1
    if n == 1:
        return fibonacci
    elif n == 2:
        fibonacci[1] = 1
        return fibonacci
    fibonacci [1] = 1
    while (i+2) < n:
        fibonacci [i+2] = fibonacci [i+1] + fibonacci [i]
        i += 1
    
    return fibonacci
        