numeros = []

a = int(input("digite um numero maior que zero: "))
while a > 0:
    numeros.append(a)
    a = int(input("digite um numero maior que zero: "))
numeros.reverse(numeros)
print(numeros.reverse)