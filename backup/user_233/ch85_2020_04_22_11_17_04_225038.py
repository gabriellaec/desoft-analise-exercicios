arquivo = open('macacos-me-mordam.txt')

ocorrencias = 0

for line in arquivo:
    
    for palavra in line.lower().split(' '):
        
        #print(palavra)
        if palavra == 'banana': ocorrencias += 1
        
arquivo.close()

print(7)