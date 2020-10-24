with open ("dados.csv", "r") as cvs:
    conteudo = cvs.read().replace(",", "\t")
    with open ("dados.tsv", "w") as tsv:
        tsv.write(conteudo)