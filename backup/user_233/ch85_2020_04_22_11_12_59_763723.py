arquivo = open('macacos-me-mordam.txt')

ocorrencias = 0

for line in arquivo:
    
    if line.lower() == 'banana': ocorrencias += 1

print(ocorrencias)