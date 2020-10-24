convertor_tsv = open('dados.csv', 'r')
csv_read = convertor_tsv.read()
csv_split = csv_read.split()
csv_join = csv_split.join('\t')

with open('dados.tsv', 'w') as arquivo_tsv:
    tsv_write = arquivo_tsv.write(csv_join)
    
convertor_tsv.close()
    