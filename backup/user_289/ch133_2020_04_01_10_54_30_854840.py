FUNCIONA = input('Está funcionando?(n/s)')
if FUNCIONA == 's':
    print('Sem problemas')
else:
    print(input('Você sabe corrigir?(n/s)'))
    
FUNCIONA2 = input('Você sabe corrigir?(n/s)')
if FUNCIONA2 == 's':
    print('Sem problemas')
else:
    print(input('Você precisa corrigir?(n/s)'))

FUNCIONA3 = input('Você precisa corrigir?(n/s)')
if FUNCIONA3 == 's':
    print('Apague tudo e tente novamente')
else:
    print ('Sem problemas')