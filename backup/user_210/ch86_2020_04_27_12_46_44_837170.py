with open("dados.csv", "r") as file:
    conteudo = file.read().split(",")
    with open("dados.tsv", "w") as dados:
        dados.write("\t".join(conteudo))