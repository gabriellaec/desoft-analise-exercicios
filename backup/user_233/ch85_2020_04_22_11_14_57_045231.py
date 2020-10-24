arquivo = open('macacos-me-mordam.txt')

ocorrencias = 0

for line in arquivo:
    
    if 'banana' in line.lower(): ocorrencias += 1
    print(line)
        
arquivo.close()

print(ocorrencias)