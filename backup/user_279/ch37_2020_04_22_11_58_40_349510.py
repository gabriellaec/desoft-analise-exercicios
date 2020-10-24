SENHA = True
while SENHA:
    tentativa = input('Qual a senha? ')
    if tentativa == 'desisto':
        print ('Você acertou a senha!')
        SENHA = False
    else:
        print('Tente novamente')