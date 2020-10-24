with open("dados.csv", "r") as csv, open("dados.tsv", "w") as tsv:
    conteudo_csv=csv.read()
    conteudo_tsv=conteudo_csv.replace(",", "\t")
    