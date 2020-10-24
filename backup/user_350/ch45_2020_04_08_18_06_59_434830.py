a = []

while True:
    numero = int(input('digite um número: '))
    if numero > 0:
        a.append(numero)
    else: break
a.sort(reverse = True)
print(a)