with open ("dados.csv", "r")as csv:
    conteudo1=csv.read()
conteudo1 = csv.split(",")
conteudo2 = ("    ".join(conteudo1))
with open ("dados.tsv", "w") as tsv:   
    tsv.write(conteudo2)