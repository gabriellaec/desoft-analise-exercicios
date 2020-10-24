a=input('Está funcionando?')
if a=='s':
    print('Sem problemas!')
elif a=='n':
    b=input('Você sabe corrigir?(n/s)')
    if b=='s':
        print('Sem problemas!')
    elif b=='n':
        c=input('Você precisa corrigir?(n/s)')
        if c=='s':
            print('Apague tudo e tente novamente')
        else:
            print('Sem problemas!')
                   
    