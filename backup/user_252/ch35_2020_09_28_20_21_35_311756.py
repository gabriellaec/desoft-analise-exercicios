numero = int(input('Digite um número: '))
s=0
while numero != 0:
    s+=numero
    numero = int(input('Digite um número: '))
if numero == 0:
    print(s)