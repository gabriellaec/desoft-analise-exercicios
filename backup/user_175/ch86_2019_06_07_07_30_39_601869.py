with open("dados.csv", 'r') as dados_csv:
    arquivo_temporario = dados_csv.read()
arquivo_temporario = arquivo_temporario.replace(",","")
with open("dados.tsv","w") as dados_tsv:
    dados_tsv.write(arquivo_temporario)