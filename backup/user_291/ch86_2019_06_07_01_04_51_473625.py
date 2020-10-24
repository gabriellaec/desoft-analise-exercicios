with open("dados.csv", "r") as CSV:
    c = CSV.read()

tsv = c.replace(',',' ')

with open("dados.tsv", "w") as TSV:
    TSV.write(tsv)
    