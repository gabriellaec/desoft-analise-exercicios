tem_duvidas = True

while tem_duvidas:
    print('Você tem dúvidas?')
    reposta_do_aluno = input()

    if reposta_do_aluno != 'não':
        print('Pratique mais')
    else:
        tem_duvidas = False

print('Até a próxima')