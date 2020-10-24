a = input('O programa está funcionando?')

if a == 's':
    print('Sem problemas!')
else:
    b = input('Você sabe corrigir? (n/s)')
    if b == 's':
        print('Sem problemas!')
    else:
        c = input("Você precisa corrigir? (n/s)")
        if c == 'n':
            print('Sem problemas!')
        else:
            print("Apague tudo e tente novamente')