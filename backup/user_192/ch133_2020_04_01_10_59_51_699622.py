resposta1 = str(input('Está funcionando? '))
if resposta1 == 's':
    print('Sem problemas!')
else:
    resposta2 = str(input('Você sabe corrigir? (n/s)'))
    if resposta2 == 's':
        print('Sem problemas!')
    else:
        resposta3 = str(input('Você precisa corrigir? (n/s)'))
        if resposta3 == 's':
            print('Apague tudo e tente novamente')
        else:
            print('Sem problemas!')