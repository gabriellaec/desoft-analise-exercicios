tem_duvidas = True
while tem_duvidas == True:
    resp = input('Possui alguma duvida na disciplina?')
    if resp != 'nao':
        print('Pratique mais')
    if resp == 'não':
        tem_duvidas = False
if tem_duvidas==False:
    print('Até a proxima')


