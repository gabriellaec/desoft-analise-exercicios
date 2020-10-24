tem_duvidas = True

if tem_duvidas:
    resposta_do_aluno = input('Você está com dúvidas? ')

    if resposta_do_aluno != 'não':
        print('Pratique mais')
        resposta_do_aluno = input('Você está com dúvidas? ')
        tem_duvidas = False
    else:
        print('Até a próxima')



