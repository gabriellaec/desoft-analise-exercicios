with open("dados.csv", 'r') as dados_csv:
    arquivo_temporario = dados_csv.read()
with open("dados.tsv","w") as dados_tsv:
    while arquivo_temporario.find(",") != -1:
        dados_tsv.write(arquivo_temporario.replace(",","\t"))
   	