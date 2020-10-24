arquivo = open('dados.csv')

elementos = []

for line in arquivo:
    
    elementos.append(line.split(','))
    
print(elementos)
    
    
arquivo.close()