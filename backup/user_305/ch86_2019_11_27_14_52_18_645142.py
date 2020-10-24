import csv
with open("dados.csv","r") as arquivo_csv:
    csv_reader = csv.reader(arquivo_csv)
    
    with open ("dados.tsv","w") as arquivo_tsv:
        csv_writer = csv.writer(arquivo_tsv, delimiter = "	")
        
        for linha in csv_reader:
            csv_writer.writerow(linha)