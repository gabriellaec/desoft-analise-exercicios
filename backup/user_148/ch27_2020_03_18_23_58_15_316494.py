tem_duvidas = True
while tem_duvidas:
    resposta_do_aluno = input('Aluno, você tem dúvidas sobre a disciplina? ')
    if resposta_do_aluno=='sim':
        print('Pratique mais')
    else:
        tem_duvidas = False
        print('Até a próxima')