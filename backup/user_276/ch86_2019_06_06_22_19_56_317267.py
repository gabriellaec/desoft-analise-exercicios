with open(dados.csv, 'w') as arquivo:
    conteudo = arquivo.read
    for linha in conteudo:
        i = 0
        for letra in linha:
            if letra == ',':
                letra = '\t'        