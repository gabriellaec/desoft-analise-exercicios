with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
palavras = conteudo.split(' ' or ',')
qtd = len(palavras) 
print(qtd)