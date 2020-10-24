with open("dados.csv","r") as csv:
    arquivo_csv = csv
    
tsv_arq = arquivo_csv.replace(',','\t')

with open("dados.csv","w") as tsv:
    tsv.write(tsv_arq)