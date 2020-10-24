senha = 'desisto'
palavra = input('Digite a palavra: ')

while palavra != senha:
    palavra = input('Digite a palavra: ')
    if palavra == senha:
        print('Você acertou a senha!')