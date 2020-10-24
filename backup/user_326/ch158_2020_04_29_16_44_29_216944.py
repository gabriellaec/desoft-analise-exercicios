with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
lista_de_palavras = conteudo.split()
numero_de_palavras = len(lista_de_palavras)