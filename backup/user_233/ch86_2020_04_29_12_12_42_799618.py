arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    linhas.append('	'.join(linha.split(',')))

print(linhas)

arquivo.close()

arquivo = open('dados.tsv', 'w')

for linha in linhas:
    arquivo.write(linha)

arquivo.close()

