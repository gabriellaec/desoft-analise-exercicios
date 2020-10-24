tem_duvidas = True

while tem_duvidas:
    print('Você tem dúvidas?')
    reposta_do_aluno = input()

    if reposta_do_aluno == 'não':
        tem_duvidas = False
    else:
        print('Pratique mais')

print('Até a próxima')