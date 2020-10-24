with open('macacos-me-mordam.txt') as arquivo:
    conteudo=arquivo.read()
    conteudo=conteudo.upper()
i=0
for d in conteudo:
    if d=='BANANA':
        i+=1
print(i)
        