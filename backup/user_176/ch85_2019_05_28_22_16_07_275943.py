with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.read()
i=0
for linha in texto:
    if linha.upper() == 'BANANA':
        i+=1
print(i)