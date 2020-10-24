funciona = input('Seu programa está funcionando? (s/n) ')
if funciona == 's':
    print('Sem problemas!')
elif funciona == 'n':
    correcao = input('Você sabe corrigir? (s/n) ')
    if correcao == 's':
        print('Sem problemas!')
    if correcao == 'n':
        necessidade = input('Você precisa corrigir? (s/n) ')
        if necessidade == 's':
            print('Apague tudo e tente novamente')
        elif necessidade == 'n':
                  print('Sem problemas!')