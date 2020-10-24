with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
tx=conteudo.split()
x=0
for i in tx:
    ii=i.lower()
    if ii=='banana':
        x+=1
    print(x)