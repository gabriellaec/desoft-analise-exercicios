with open('macacos-me-mordam.txt','r') as file:
    linhas = file.readlines()
    
cont = 0
for linha in linhas:
    palavras = linha.split(' ')
    for palavra in palavras:
        if palavra.upper() == 'BANANA':
            cont += 1
print(cont)