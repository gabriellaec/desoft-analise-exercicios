with open("dados.csv","r") as arquivo:
    conteudo= arquivo.read()
conteudo.replace(",","	")
with open("dados.tsv","a") as tsv:
    tsv.append(conteudo)