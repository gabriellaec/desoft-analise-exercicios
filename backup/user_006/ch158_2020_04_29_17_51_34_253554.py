with open('textto.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    palavras=conteudo.split()
print(palavras)