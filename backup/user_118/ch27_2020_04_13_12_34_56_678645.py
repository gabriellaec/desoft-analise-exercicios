tem_duvidas = True
resposta_do_aluno=input('Você tem dúvidas na disciplina? ')
if resposta_do_aluno  != 'não':
    print ('Pratique mais!')
while tem_duvidas:
    resposta_do_aluno=input('Você tem dúvidas na disciplina? ') 
    if resposta_do_aluno =='não':
        tem_duvidas = False
print('Até a proxima!')