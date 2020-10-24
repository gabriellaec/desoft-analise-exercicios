with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
y = str(conteudo)
x = y.capitalize()
soma = 0
for i in range(len(x)):
    if x[i] == 'BANANA':
        soma+=1
print(soma)
