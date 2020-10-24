p1=input('Está funcionando?: ')
if p1 == 's':
    print('Sem Problemas!')
elif p1 == 'n':
    p2=input('Você sabe corrigir? (n/s): ')
    if p2 == 's':
        print('Sem Problemas!')
    elif p2 == 'n':
        p3 = input('Você precisa corrigir? (n/s): ')
        if p3 == 'n':
            print('Sem Problemas!')
        elif p3 == 's':
            print('Apague tudo e tente novamente')
        
       