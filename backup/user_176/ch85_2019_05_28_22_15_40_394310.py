with open('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.readlines()
i=0
for linha in texto:
    if linha.upper() == 'BANANA':
        i+=1
print(i)