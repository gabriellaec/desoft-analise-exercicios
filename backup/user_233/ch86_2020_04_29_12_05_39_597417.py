arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    linhas.append(linha.split(','))
    
elementos = []

for linha in linhas:
    for elemento in linha:
        elementos.append(elemento.strip())

print(elementos)

arquivo.close()

arquivo = open('dados.tsv', 'x')

