contador = 0
n = 0
lista = []
while n != 1:
    if n % 2 == 0:
        n = n/2
    else:
        n = 3 * n + 1
    contador += 1
    n += 1
    