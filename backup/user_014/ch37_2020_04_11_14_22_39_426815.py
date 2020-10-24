descobrindo_senha = True

while descobrindo_senha:
    senha = input('Qual é a senha? ')
    if senha != 'desisto':
        descobrindo_senha = True
    else:
        descobrindo_senha = False
print('Você acertou a senha')