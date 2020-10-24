with open('dados.csv', 'r') as arquivo_csv:
    texto = arquivo_csv.read()
tsv = csv.loads(texto)
arquivo_tsv.write(tsv)
 