# Construindo fluxograma

condicao = True
while condicao:
    print('Seu programa está funcionando? Responda s para sim ou n para não')
    resposta1 = input()
    print('')

    if resposta1 == 's':
        print('Sem problemas!')
        condicao = False
        print('')
    elif resposta1 == 'n':
        print('Voçê sabe corrigir? Responda s para sim ou n para não')
        resposta2 = input()
        print('')

        if resposta2 == 's':
            print('Sem problemas!')
            condicao = False
            print('')
        elif resposta2 == 'n':
            print('Você precisa corrigir? Responda s para sim ou n para não')
            resposta3 = input()
            print('')

            if resposta3 == 's':
                print('Apague tudo e tente novamente')
                condicao = False
                print('')
            elif resposta3 == 'n':
                print('Sem problemas!')
                condicao = False
                print('')