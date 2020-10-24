x = int(input('numero: '))
soma = 0
y = True
while y:
    if x != 0:
        soma = soma + x
        x = int(input('numero: '))
        y = True
    elif x == 0:
        y = False
print (soma)