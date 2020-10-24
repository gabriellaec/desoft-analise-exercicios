with open('dados.csv', 'r') as arquivo:
    csv=arquivo.read().split(',')
    tsv='\t'.join(csv)
with open('dados.tsv', 'w') as arquivo:
    arquivo.write(tsv)
 
    