arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    linhas.append(linha.split(','))
    
elementos = []
novas_linhas = []

for linha in linhas:
    nova_linha = '\t'.join(linha)
    novas_linhas.append(nova_linha)

print(linhas)

linhas = []

arquivo.close()

arquivo = open('dados.tsv', 'x')

