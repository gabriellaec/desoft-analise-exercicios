x = True
lis = []

while x:
    z = int(input('digite numeros, e digite zero ou negativo para parar: '))
    lis.append(z)
    if z<=0:
        x = False

a=lis.sort(reverse=True)

print(a)