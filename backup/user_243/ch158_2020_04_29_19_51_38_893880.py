def x(nome):
    with open (nome,'r') as arquivo:
        conteudo=arquivo.read()
        palvaras=conteudo.split()
        return len(palavras)
print(x("texto.txt"))