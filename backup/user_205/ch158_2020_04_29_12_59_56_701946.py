with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
x = conteudo.split()
print (len(x))