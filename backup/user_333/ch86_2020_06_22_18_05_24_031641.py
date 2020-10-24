with open('dados.csv', 'r') as dados_csv:
    dados_c = arquivo_csv.read()
    
dados=dados_j.split(',')
dados_t = '\t'.join(dados)

with open('dados.tsv', 'w') as dados_tsv:
    arquivo_tsv.write(dados_t)
