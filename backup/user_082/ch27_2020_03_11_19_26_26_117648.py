
tem_duvidas= True
while tem_duvidas:
    pergunta_aluno= input('Voce tem alguma duvida? ')
    if pergunta_aluno != 'não':
        print('Pratique mais')
    else:
        tem_duvidas= False
print("Até a próxima")