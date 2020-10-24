não_é_0 = True

soma = 0

while não_é_0:
    n = int(input('digite um numero: '))
    if n != 0:
        soma += n
    else:
        não_é_0 = False
else:
    print(soma)
