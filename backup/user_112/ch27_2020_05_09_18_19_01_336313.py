tem_duvidas = True

if tem_duvidas:
    resposta_do_aluno = input('tem duvida?')

    while resposta_do_aluno != 'não':
        print("Pratique mais")
    
    else: 
        print("Até a próxima")
        tem_duvidas = False
        