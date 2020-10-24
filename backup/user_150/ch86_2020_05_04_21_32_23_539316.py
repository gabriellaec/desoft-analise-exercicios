with open('dados.csv', 'r') as arquivo:
    leitura = arquivo.readlines()

for palavras in leitura:
    separador = palavras.split(',')
    for palavra in separador:
        juntar = palavra.join('\t')