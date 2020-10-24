with open('dados.csv', 'r') as f:
    arquivo = f.read()

x = arquivo.split(',')
x = x.join('	')

with open('dados.tsv', 'w') as f:
    f.write(x)
    