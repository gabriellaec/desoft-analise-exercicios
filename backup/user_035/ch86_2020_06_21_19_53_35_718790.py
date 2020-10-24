with open("dados.csv","r") as csv:
    conteudo = csv.read().replace(",", " ")
    with open("dados.tsv","w") as tsv:
        tsv.write(conteudo)
