tem_duvidas = True

print('Você tem dúvidas?')
while tem_duvidas:
    reposta_do_aluno = input()

    if reposta_do_aluno == 'não':
        
        tem_duvidas = False
    else:
        print('Pratique mais')

print('Até a próxima')