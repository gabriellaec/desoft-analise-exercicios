with open('texto.txt', 'r') as texto:
    conteudo = texto.read()
n = conteudo.split()
print (len(n)) 