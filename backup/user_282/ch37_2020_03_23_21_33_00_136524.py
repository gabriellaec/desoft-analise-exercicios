resposta = True


while resposta:
     guess = input('digite a senha: ')
     if guess == 'desisto':
         resposta = False
     else:
         print()
else:
    print('Você acertou a senha!')