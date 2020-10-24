senha = 'desisto'
palavra = input('Tente acertar a senha. Digite uma palavra:')
while palavra != senha:
    print('Tente novamente')
    palavra = input('Tente acertar a senha. Digite uma palavra:')
print('Você acertou a senha!')