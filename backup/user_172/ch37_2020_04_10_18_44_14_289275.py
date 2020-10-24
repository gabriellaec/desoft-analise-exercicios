senha = input('qual a senha? ')
y = True
while y:
    if senha == 'desisto':
        print ('Você acertou a senha!')
        y = False
    else:
        senha = input('qual a senha? ')