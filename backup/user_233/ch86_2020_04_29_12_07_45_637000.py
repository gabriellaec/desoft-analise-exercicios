arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    linhas.append(linha.split(','))
    
elementos = []

for linha in linhas:
    linha = '\t'.join(linha)

print(linhas)

linhas = []

arquivo.close()

arquivo = open('dados.tsv', 'x')

