n = input() #recebendo o número
if n == '':
    n = 1
i = 1 #número de termos
while n != 1:
    n = int(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
    i += 1
print(i)