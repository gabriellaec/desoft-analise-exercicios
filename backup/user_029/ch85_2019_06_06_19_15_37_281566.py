with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
cs = conteudo.split()
soma = 0
for i in cs:
    minusculo = i.lower()
    if minusculo == 'banana':
        soma += 1
print(soma)

    
    