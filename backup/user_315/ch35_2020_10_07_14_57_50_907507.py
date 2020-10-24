numero = int(float('digite um numero: '))
s=0
while numero != 0:
    s += numero
    numero = int(float('digite um numero: '))
    if numero == 0:
        print (s)