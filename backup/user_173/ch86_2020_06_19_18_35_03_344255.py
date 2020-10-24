with open('dados.csv','r') as arquivo_csv:
    leitura = arquivo_csv.read()
    csv_para_tsv = leitura.replace(',','\t')
    with open('dados.tsv','w') as arquivo_tsv:
        escreve = arquivo_tsv.write(csv_para_tsv)
    