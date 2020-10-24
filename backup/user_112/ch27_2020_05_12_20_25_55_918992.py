tem_duvidas = True

if tem_duvidas:
    resposta_do_aluno = input('você está com dúvidas? ')
    
    while resposta_do_aluno == 'não':
        print('parabéns')
        tem_duvidas = False
    else: 
        print('Pratique mais')