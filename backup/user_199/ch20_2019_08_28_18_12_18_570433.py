todo_mundo_odeia_o_chris=True
x=str(input('qual seu nome: '))
while todo_mundo_odeia_o_chris:
    if x=='chris':
        print ('todo mundo odeia o chris')
        break
        
    else:
        print('Olá, {0}'.format(x))
        todo_mundo_odeia_o_chris=False
        break
        
    