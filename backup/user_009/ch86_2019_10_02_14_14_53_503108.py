import csv
while open('dados.csv','r') as csv_file:
    csv_reader = csr.reader(csv_file)
    
    
    with open('new_names.csv','w') as dados.tsv:
        csv_writer = csv.writer(dados.tsv, delimiter = '\t')
    
    
    for line in csv_reader:
        dados.tsv.writerow(line)