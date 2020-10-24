with open ('dados.csv', 'r') as arquivocsv:
    conteudocsv = arquivocsv.read()
    conteudotsv = conteudocsv.replace(',', '\t')
with open ('dados.tsv', 'w') as arquivotsv:
    arquivotsv.write(conteudotsv)
    print(arquivotsv)
    