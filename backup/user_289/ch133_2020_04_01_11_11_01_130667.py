input('Está funcionando?(n/s)')
FUNCIONA = input('Está funcionando?(n/s)')
if FUNCIONA == 's':
    print('Sem problemas')
elif FUNCIONA == 'n':
    FUNCIONA2 = input('Você sabe corrigir?(n/s)')
    input('Você sabe corrigir?(n/s)')
    if FUNCIONA2 == 's':
        print('Sem problemas')
    elif FUNCIONA2 == 'n':
        FUNCIONA3 = input('Você precisa corrigir?(n/s)')
        input('Você precisa corrigir?(n/s)')
        if FUNCIONA3 == 's':
            print('Apague tudo e tente novamente')
        elif FUNCIONA3 == 'n':
            print ('Sem problemas')