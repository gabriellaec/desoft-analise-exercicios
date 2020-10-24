with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    conteudo = arquivo.lower()
    split = conteduo.split()
    i = 0
for palavra in split:
    if palavra == 'banana':
        i +=1
print(i)