arquivo = open('macacos-me-mordam.txt')

ocorrencias = 0

for line in arquivo:
    
    for palavra in line.lower().split(' '):
        
        if palavra == 'banana': ocorrencias += 1
        
arquivo.close()

print(ocorrencias)