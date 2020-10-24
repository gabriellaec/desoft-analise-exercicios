with open("dados.csv","r") as arquivo:
    conteudo= arquivo.read()
with open("dados.tsv","w") as tsv:
    arquivo.write("conteudo")