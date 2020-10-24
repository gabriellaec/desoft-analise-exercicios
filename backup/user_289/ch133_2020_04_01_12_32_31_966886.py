input('Está funcionando?(n/s)')
if 's':
    print('Sem problemas!')
else:
    input('Você sabe corrigir?(n/s)')
    if 's':
        print('Sem problemas')
    else: 
        input('Você precisa corrigir?(n/s)')
        if 's':
            print('Apague tudo e tente novamente')
        else:
            print ('Sem problemas')