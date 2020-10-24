x=0
arquivo= open('macacos-me-mordam.txt','r')
conteudo= arquivo.read()
conteudo= conteudo.lower()
for i in conteudo:
    if i== 'banana':
        x+=1
print(x)