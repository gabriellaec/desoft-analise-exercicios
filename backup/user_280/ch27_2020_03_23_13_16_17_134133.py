tem_duvidas = True
while tem_duvidas:
    resposta_do_aluno = input ('Você está com dúvidas? ')
    if resposta_do_aluno == 'não':
        print ('ok')
        tem_duvidas = False
    else:
        print ('Pratique mais')