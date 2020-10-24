with open('texto.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    palavra=conteudo.split()
print(palavra)
    