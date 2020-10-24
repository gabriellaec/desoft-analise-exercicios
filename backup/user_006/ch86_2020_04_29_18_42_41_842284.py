with open("dados.csv", "a") as arquivo:
    conteudo=arquivo.read()
    dados.tsv=conteudo.replace(",", "	")
    