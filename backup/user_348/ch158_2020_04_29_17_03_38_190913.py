with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    quantidade_de_palavras = len(palavras)
    print(quantidade_de_palavras)
        