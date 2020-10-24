loop = True

while loop:
    ask = input('Qual a senha? ')
    if ask=='desisto':
        print('Você acertou a senha!')
        loop = False
    else:
        print('Tente denovo')
