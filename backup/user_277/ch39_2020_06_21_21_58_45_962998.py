lista = []
contador1 = 0
numero = 0
contador2 = 0

for n in range(1,1001):
    while n<0:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        contador1 +=1

        if contador1 > contador2:
            contador1 = contador2
            numero = n
print (numero)