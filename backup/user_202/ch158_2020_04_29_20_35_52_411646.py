with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    texto.split(' ')
    print(len(texto))
    