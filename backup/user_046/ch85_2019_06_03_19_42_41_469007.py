with open('macacos-me-mordam.txt') as arquivo:
    conteudo=arquivo.read()
    
i=0
for d in conteudo:
    if d.lower()=='BANANA':
        i+=1
print(i)
        