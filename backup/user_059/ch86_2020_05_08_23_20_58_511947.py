import csv

with open('dados.csv') as arquivo:
    reader = csv.reader(arquivo)
    
novo = open('dados.tsv', 'w')
novo.write(reader, delimiter = '	')
novo.close
    
    
    
    
