arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    linhas.append('\t'.join(linha.split(',')))

print(linhas)

arquivo.close()

arquivo = open('dados.tsv', 'x')

