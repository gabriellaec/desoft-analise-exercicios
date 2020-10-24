with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

lista = conteudo.split()
palavras = len(lista)
print(palavras)