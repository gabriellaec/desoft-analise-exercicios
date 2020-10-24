x = float(input('Digite um numero:'))
soma=1
while x != 0:
    soma+=x
    x = float(input('Digite um numero:'))
    if x == 0:
        print(soma)
    