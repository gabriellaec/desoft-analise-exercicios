def x(nome):
    with open (nome,'r') as arquivo:
        conteudo=arquivo.read()
        palavras=conteudo.split()
        return len(palavras)
print(x("texto.txt"))