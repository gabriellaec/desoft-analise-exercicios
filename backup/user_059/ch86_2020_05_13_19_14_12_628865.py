with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    troca = conteudo.replace(',', '\t')
    with open('dados.tsv', 'w') as arquivo2:
        r = arquivo2.write(troca)
    
    
