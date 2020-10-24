with open('dados.csv', 'r') as f:
    arquivo = f.read()

x = arquivo.split(',')
x = '	'.join(x)

with open('dados.tsv', 'w') as f:
    f.write(x)
    