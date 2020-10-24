arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    linhas.append(linha.split(','))
    
elementos = []
novas_linhas = []

for linha in linhas:
    nova_linha = '	'.join(linha)
    novas_linhas.append(nova_linha)

print(novas_linhas)

linhas = []

arquivo.close()

arquivo = open('dados.tsv', 'x')

