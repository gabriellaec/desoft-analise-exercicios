with open('dados.csv','r') as arquivo:
    dados = arquivo.read()
dados = dados.replace(',','\t')
with open('dados.tsv','w') as tsv:
    tsv.write(dados)