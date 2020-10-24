with open(dados.csv, 'w') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for linha in conteudo:
        i = 0
        for letra in linha:
            if letra == ',':
                letra = '\t'        