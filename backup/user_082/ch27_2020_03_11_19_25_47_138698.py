tem_duvidas= True
while tem_duvidas:
    pergunta_aluno= input('Voce tem alguma duvida na disciplina? ')
    if pergunta_aluno != 'não':
        print('Pratiquei mais')
    else:
        tem_duvidas= False
print("Até a próxima")