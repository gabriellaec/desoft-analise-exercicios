with open("dados.csv","r") as csv:
    arquivo_csv = csv
    
tsv = arquivo_csv.replace(',','	')

with open("dados.csv","w") as tsv:
    tsv.write(tsv)