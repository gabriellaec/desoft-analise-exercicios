a = []
while a > 0:
    numero = int(input('digite um número: '))
    a.append(numero)
    
a.sort(reverse = True)
print(a)