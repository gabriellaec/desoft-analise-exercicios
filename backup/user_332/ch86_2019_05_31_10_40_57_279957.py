with open("dados.csv","r") as csv:
    arquivo_csv = csv
    
csv = arquivo_csv.split()

with open("dados.csv","w") as tsv:
    tsv.write(csv)