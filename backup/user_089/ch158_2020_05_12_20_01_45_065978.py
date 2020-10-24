with open("texto.txt","r") as arquivo:
    conteudo = arquivo.read()
    a = conteudo.split()
print(len(a))