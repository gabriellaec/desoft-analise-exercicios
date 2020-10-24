with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()

x = list(conteudo)
soma = 0
for i in range(len(x)):
    if x[i] == 'banana' or 'Banana' or 'BANANA' or 'BaNaNa':
        soma+=1
print(soma)
