with open ("dados.csv", "r") as csv:
    ler = csv.read()
    x = ler.split()
    for i in x:
        if i == ",":
            i.replace("\t")
with open ("dados.tsv", "w") as tsv:
    esc = tsv.write(x)
            