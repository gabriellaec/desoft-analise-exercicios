with open('macacos_me_mordam.txt','r') as arquivo:
    conteudo = arquivo.read().split()
x = 0
for i in conteudo:
    palavra = i.lower()
    if palavra == 'banana':
        x += 1
print(x)