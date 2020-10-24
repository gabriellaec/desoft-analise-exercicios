Perg_1 = input('Está funcionando?')
Perg_2 = input('Você sabe corrigir? (n/s)')
if Perg_2 == 's':
    print('Sem problemas!')
else:
    Perg_3 = input('Você precisa corrigir? (n/s)')
    if Perg_3 == 's':
        print('Apague tudo e tente novamente')
    else:
        print('Sem problemas!')
    
    