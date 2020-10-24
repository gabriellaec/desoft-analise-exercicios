with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo= arquivo.read()
    
x = conteudo.lower()
y=x.split()
contador[0]=0
for i in range(len(y)):
    if y[i]=='banana':
        contador+=1