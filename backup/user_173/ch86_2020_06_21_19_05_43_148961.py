with open('dados.csv','r') as arquivo:
    leitura = arquivo.read()
    csv_para_tsv = leitura.replace(',','\t')
with open('dados.tsv','w') as arquivoTsv:
    escrever = arquivoTsv.write(csv_para_tsv)
    