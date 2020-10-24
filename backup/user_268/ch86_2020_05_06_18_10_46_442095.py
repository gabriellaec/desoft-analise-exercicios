with open("dados.csv", "r") as arq:
    cont = arq.read()
    new = cont.replace("," , "\t")
with open("dados.tsv", "w") as arq:
    arq.write(new)






























