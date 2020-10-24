sum = 0
n = 1
while n != 0:
    numero = int(input('Digite um número: '))
    if numero == 0:
        n = 0
    else:
        sum += numero
if numero == 0:
    print(sum)
