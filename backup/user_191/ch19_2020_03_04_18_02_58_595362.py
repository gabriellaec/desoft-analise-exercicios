a=int(input('Lado 1:'))
b=int(input('Lado 2:'))
c=int(input('Lado 3:'))
if a==b:
    if b==c:
        print('equilátero')
    else:
        print('isósceles')
elif b==c:
    print('isósceles')
else:
    print('escaleno')