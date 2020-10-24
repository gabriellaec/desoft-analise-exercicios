with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    final = conteudo.split()
    
print(len(final))