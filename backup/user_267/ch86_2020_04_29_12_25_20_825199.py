import csv
with open('dados.csv', 'r') as arquivo_csv:
    texto = arquivo_csv.read()
print(texto)
tsv = csv.loads(texto)
with open('dados.tsv', 'w') as arquivo_tsv:
    arquivo_tsv.write(tsv)
 