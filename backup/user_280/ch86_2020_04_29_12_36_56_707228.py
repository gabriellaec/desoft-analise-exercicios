def csv_para_tsv(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        trocado = conteudo.replace(',', '	')
    with open('dados.tsv', 'w') as arquivo2:
        arquivo2.write(trocado)
    return trocado

tsv = csv_para_tsv('dados.csv')
