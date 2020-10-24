game_on=True
while game_on==True:
    p=input('qual a senha? ')
    if p=='desisto':
        game_on=False
    else:
        print('voce errou tente novamente')
print('Você acertou a senha!)