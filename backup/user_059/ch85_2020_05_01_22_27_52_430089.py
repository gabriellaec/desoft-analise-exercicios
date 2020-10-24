with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()

soma = 0
for i in range(len(conteudo)):
    if conteudo[i] == 'banana' or 'Banana' or 'BANANA' or 'BaNaNa':
        soma+=1
print(soma)
