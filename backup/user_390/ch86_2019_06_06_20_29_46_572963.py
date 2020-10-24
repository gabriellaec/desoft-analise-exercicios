with open("dados.csv","r") as arquivo:
    conteudo= arquivo.read()
conteudo = conteudo.replace(",","	")
with open("dados.tsv","a") as tsv:
    tsv.write(conteudo)