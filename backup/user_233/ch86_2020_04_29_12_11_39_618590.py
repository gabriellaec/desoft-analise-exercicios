arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    linhas.append('	'.join(linha.split(',')))

print(linhas)

arquivo.close()

arquivo = open('dados.tsv', 'x')

for linha in linhas:
    arquvio.write(linha)

arquivo.close()

