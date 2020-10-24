with open('dados.tsv', 'w') as TSV:
    
    with open('dados.csv', 'r') as CSV:
        conteudo = CSV.read()
        conteudo = conteudo.replace(',', '\t')
        TSV.write(conteudo)