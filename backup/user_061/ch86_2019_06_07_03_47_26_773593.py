csv = open("dados.csv", "r", encoding="utf8").read()
tsv = open("dados.tsv", "w", encoding="utf8").write(csv.replace(",","\t"))