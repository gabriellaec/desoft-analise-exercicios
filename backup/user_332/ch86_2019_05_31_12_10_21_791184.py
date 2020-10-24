with open("dados.csv","r") as csv:
    arquivo_csv = csv.read()
    
tsv_arq = arquivo_csv.replace(',','	')

with open("dados.tsv","w") as tsv:
    tsv.write(tsv_arq)