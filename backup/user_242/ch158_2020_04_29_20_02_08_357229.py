with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = arquivo.split()
    return len(palavras)