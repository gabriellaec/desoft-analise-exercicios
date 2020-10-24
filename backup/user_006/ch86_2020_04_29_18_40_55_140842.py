with open("dados.csv", "r") as arquivo:
    conteudo=arquivo.read()
    dados.tsv=conteudo.replace(",", "	")
    