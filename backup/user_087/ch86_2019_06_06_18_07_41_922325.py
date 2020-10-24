with open ('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    
    with as ('dados.tsv', 'r') as arq:
        conteudo = arq.read()