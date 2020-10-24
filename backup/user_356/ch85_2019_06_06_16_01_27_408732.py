with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
tx=texto.split()
x=0
for i in conteudo:
    ii=i.lower()
    if ii=='banana':
        x+=1
    print(x)