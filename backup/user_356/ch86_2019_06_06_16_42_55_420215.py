with open('dados.csv', 'r') as csv:
    ler_csv=csv.read()
with open('dados.tsv', 'w') as tsv:
    tsv_writer = tsv.write('ler_csv\n')