with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    
    with open ('dados.tsv', 'r') as arq:
        conteudo = arq.read()