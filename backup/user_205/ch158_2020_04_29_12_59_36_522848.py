with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
x = conteudo.split()
return len(x)