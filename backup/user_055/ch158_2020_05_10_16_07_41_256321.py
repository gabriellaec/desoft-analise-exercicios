with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = len(conteudo.split(' ')) + 3
    print(palavras)