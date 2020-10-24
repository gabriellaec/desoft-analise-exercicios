tem_duvida=True
while(tem_duvida):
    c=input('voce tem alguma duvida na disciplina: ')
    if c != 'não':
        print('Pratique mais')
    else:
        tem_duvida=False
print('Até a próxima')