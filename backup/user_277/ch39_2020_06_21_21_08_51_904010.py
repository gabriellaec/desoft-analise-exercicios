contador = 0
n = 0
while n != 1:
    if n % 2 == 0:
        n = n/2
    else:
        n = 3 * n + 1
    contador = contador + 1
    n= n + 1
    