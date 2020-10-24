with open ('dados.csv', 'r') as arquivo:
    texto = arquivo.read()
    valores = texto.split(',')
with open ('dados.tsv', 'w') as arquivo:
    valor = '\t'.join(valores)
    arquivo.write(valor)