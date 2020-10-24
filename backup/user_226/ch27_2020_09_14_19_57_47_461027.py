game_on = True

while game_on:
    resposta = input('voce tem duvidas? ')
    if resposta != 'não':
        print('Pratique mais')
    else:
        game_on = False

print('Até a próxima')