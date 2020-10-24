resposta1 = input('O programa está funcionando? (s/n) ')
if resposta1 == 's':
    print('Sem problemas! ')
else:
    resposta2 = input('Você sabe corrigir? (s/n) ')
    if resposta2 == 's':
        print('Sem problemas! ')
    else: 
        resposta3 = input('Você precisa corrigir? (s/n) ')
        if resposta3 == 's':
            print('Apague tudo e tente novamente')
        else: 
            print('Sem problemas!')