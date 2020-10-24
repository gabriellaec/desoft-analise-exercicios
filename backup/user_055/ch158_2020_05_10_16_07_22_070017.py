with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = len(conteudo.split(' '))
    print(palavras)