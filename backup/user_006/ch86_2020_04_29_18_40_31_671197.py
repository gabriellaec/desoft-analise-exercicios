with open("dados.csv", "w") as arquivo:
    conteudo=arquivo.read()
    dados.tsv=conteudo.replace(",", "	")
    