senha = str(input('Escreva uma senha: '))

while senha != 'desisto':
    print('Essa não é a senha correta.')
    senha = str(input('Escreva uma senha válida: '))

print('Você acertou a senha!')