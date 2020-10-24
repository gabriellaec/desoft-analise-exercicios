r1 = input ('Está funcionando?')
if r1 == 's':
    print ('Sem problemas!')
elif r1 == 'n':
    input ('Você sabe corrigir?')
    if r1 == 's':
        print('Sem problemas!')
    elif r1 == 'n':
        input ('Você precisa corrigir?')
        if r1 == 's':
            print ('Apague tudo e tente novamente')
        else:
            print('Sem problemas!')