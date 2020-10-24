lista = []
x = 1
while x > 0:
    a = int(input('escolha um numero '))
    if a <= 0:
        x-=1
    if a > 0:
        lista.append(a)
lista.reverse()