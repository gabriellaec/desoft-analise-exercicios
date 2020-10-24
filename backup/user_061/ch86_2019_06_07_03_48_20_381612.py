csv = open("dados.csv", "r", encoding="utf8").read()
with open("dados.tsv", "w", encoding="utf8") as tsv:
	tsv.write(csv.replace(",","	"))