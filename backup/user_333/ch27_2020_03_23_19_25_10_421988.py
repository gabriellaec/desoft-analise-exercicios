tem_duvida=True

while tem_duvida:
    resposta_do_aluno=input('Tem alguma dúvida? ')
    if resposta_do_aluno != 'não':
        tem_duvida=True
        print("Pratique mais")
    else:
        tem_duvida=False
else:
    print('Até a próxima')