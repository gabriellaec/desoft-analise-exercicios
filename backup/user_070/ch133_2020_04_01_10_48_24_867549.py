a = 0
b = 0
c = 0
while a != 'n' and a != 's':
    a = input('Está funcionando?')
if a == 's':
    print('Sem problemas!')
else:
    while b != 'n' and b != 's':
        b = input('Você sabe corrigir? (n/s)')
    if b == 's':
        print('Sem problemas!')
    else:
        while c != 'n' and c != 's':
            c = input('Você precisa corrigir? (n/s)')
        if c == 'n':
            print('Sem problemas!')
        else:
            print('Apague tudo e tente novamente')