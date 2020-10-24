import csv

with open ('dados.csv','r') as file, open('dados.tsv','w') as file_tsv:
      file=csv.reader(file)
      file_tsv=csv.writer(file_tsv, delimiter='\t')
      
      for i in file:
          file_tsv.writerow(i)

