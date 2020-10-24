programa = input('Está funcionando?(s/n): ')
if programa == 's':
    print('Sem problemas!')
else:
    correcao = input('Você sabe corrigir?(s/n): ')
    if correcao == 's':
        print('Sem problemas!')
    else:
        precisa_correcao = input('Você precisa corrigir?(s/n): ')
        if precisa_correcao == 's':
            print('Apague tudo e tente novamente')
        else:
            print('Sem problemas!')
    