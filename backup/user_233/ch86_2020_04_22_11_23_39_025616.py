arquivo = open('dados.csv')

elementos = []

for line in arquivo:
    
    elementos.append(line.split(','))
    
arquivo.close()

arquivo = open('dados.tsv', 'x')

for elemento in elementos:
    arquivo.write(elemento)
    arquivo.write('\t')

arquvio.close()