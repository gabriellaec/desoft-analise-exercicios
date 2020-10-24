with open('palavras.txt', 'a.') as arquivo:
    conteudo=arquivo.read()
palavras_com_a=conteudo.split()
print(len(palavras_com_a))