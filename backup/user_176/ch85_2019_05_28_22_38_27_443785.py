with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.readlines()
    
lista = []
for linha in texto:
    palavras = linha.split(' ')
    for palavra in palavras:
        lista.append(palavra)
i = 0
for palavra in lista:
    if palavra.upper() == 'BANANA':
        i+=1
print(i)