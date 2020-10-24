x=input('Está funcionando?')
if x=='s':
    print('S problemas!')
elif x=='n':
    y=input('Você sabe corrigir?(n/s)')
    if y=='s':
        print('Sem problemas!')
    elif y=='n':
        w=input('Você precisa corrigir?(n/s)')
        if w=='n':
            print('Sem problemas!')
        elif w=='s':
            print('Apague tudo e tente novamente')
         

