pergunta=input('Digite a senha: ')
i = True
while i:
    if pergunta !=  'desisto':
        pergunta=input('Digite a senha: ')
    else:
        i = False
        print('Você acertou a senha!')