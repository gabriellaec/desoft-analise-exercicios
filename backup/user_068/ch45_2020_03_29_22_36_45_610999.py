a = int(input('Qual o número:'))
b = []
while a > 0:
    b.append(a)
    a = int(input('Qual o número:'))
print(b.reverse())