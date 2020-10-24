with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
x = conteudo.upper()
soma = 0
for i in range(len(x)):
    if x[i] == 'BANANA':
        soma+=1
print(soma)
