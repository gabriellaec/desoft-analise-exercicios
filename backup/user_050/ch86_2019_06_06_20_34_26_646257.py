with open ("dados.csv", "r")as csv:
    conteudo=csv.read()
conteudo1 = conteudo.split(',')
conteudo2 = ("    ".join(conteudo1))
with open ("dados.tsv", "w") as tsv:   
    tsv.write(conteudo2)