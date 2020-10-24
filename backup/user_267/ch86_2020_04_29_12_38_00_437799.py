with open('dados.csv', 'r') as arquivo_csv:
    texto = arquivo_csv.read()
    s = texto.replace(',','\t')
with open('dados.tsv', 'w') as arquivo_tsv:
    arquivo_tsv.write(s)
print(arquivo_tsv)