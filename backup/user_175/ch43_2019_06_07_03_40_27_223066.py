N = 1000
n = 2
contador1 = 0
contador2 = n
maior = 0
p = n
while n <= 1000:
    contador1 = 0
    p = n
    while p != 1:
        if p%2 == 0:
            p = p/2
            contador1 += 1
        else:
            p = (3*p) + 1
            contador1 += 1
        if contador1 > maior:
            maior = contador1
            contador2 = n
    n += 1