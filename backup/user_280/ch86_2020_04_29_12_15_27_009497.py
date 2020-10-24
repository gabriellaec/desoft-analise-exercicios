def csv_para_tsv(arquivo):
    trocado = arquivo.replace(',', '    ')
    return trocado
print(csv_para_tsv('dados.csv'))