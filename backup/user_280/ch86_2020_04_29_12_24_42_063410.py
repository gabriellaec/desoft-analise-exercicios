def csv_para_tsv(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        i = 0
        while i < len(conteudo):
            if conteudo[i] == ',':
                conteudo [i] == '    '
            i+=1
    return conteudo

print(csv_para_tsv('dados.csv'))