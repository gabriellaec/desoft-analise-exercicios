p1 = str(input('Está funcionando?(s/n) '))
if p1 == 's':
    print ('Sem problemas!')
else:
    p2 = str(input('Você sabe corrigir?(s/n) '))
    if p2 == 's':
        print ('Sem problemas!')
    else:
        p3 = str(input('Você precisa corrigir? (s/n)'))
        if p3 == 's':
            print ('Apague tudo e tente novamente')
        else:
            print ('Sem problemas!')