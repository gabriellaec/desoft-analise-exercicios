with open ("dados.csv","r") as csv:
    conteudo = csv.read().replace(",","\t")
    with open ("dados.tsv","w") as tsv:
        tsv.write(conteudo)