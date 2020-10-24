num = range(0, 1001)
maior = 0
num_f = 0
for e in num:
    n = e
    cont = 0
    while n > 1:
        if n % 2 == 0:
            n *= (1/2)
            cont += 1
        else:
            n *= 3
            n += 1
            cont += 1
    if cont > maior:
        maior = cont
        num_f = e
print (num_f)
        

    