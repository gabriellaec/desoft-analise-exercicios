tem_duvidas = True

while tem_duvidas:
    resposta_do_aluno = input('você está com dúvidas? ')
    
    if resposta_do_aluno == 'não':
        print('parabéns')
        tem_duvidas = False
    else: 
        print('Pratique mais')