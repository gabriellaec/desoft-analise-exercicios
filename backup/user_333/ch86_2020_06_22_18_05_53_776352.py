with open('dados.csv', 'r') as dados_csv:
    dados_c = dados_csv.read()
    
dados=dados_c.split(',')
dados_t = '	'.join(dados)

with open('dados.tsv', 'w') as dados_tsv:
    dados_tsv.write(dados_t)
