with open('dados.csv', 'r') as csv:
    conteudo_csv=csv.read()
    separar_csv=conteudo_csv.split(',')
with open('dados.tsv', 'w') as tsv:
    mudanca=separar_csv.replace(',','	')
    tsv.write(mudanca)