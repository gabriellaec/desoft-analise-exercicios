a = int(input('Qual o número:'))
b = []
while a > 0:
    b.append(a)
    a = int(input('Qual o número:'))
if a <= 0:
print(b.reverse())