with open("dados.csv", "r", encoding="utf8") as csv:
	csv = csv.read()
with open("dados.tsv", "w", encoding="utf8") as tsv:
	tsv.write(csv.replace(",","\t"))