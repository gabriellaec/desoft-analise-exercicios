with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = arquivo.split()
    quantidade_de_palavras = len(palavras)
    print(quantidade_de_palavras)
        