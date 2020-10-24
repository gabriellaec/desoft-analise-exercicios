r1= input ('Está funcionando?')
if r1 == 's':
    print ('Sem problemas!')
elif r1 == 'n':
    r2 = input ('Você sabe corrigir?")
    if r2 == 's':
        print ('Sem problemas!')
    elif r2 == 'n':
        r3 = input ('Você precisa corrigir?')
        if r3 == 's':
            print ('Apague tudo e tente novamente')
        else:
            print ('Sem problemas!')