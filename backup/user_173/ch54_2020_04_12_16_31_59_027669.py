def calcula_fibonacci (n):
    fibonacci = []
    i = 0
    fibonacci [0] = 1
    fibonacci [1] = 1
    while i < n:
        fibonacci [i] = fibonacci [i-1] + fibonacci [i-2]
        i += 1
    
    return lista
        