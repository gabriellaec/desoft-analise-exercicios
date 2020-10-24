with open ("dados.csv","r") as csv:
    lista = csv.split(",")
    tsv = lista.join("\t")
    return tsv