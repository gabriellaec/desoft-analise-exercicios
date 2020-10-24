with open('macacos-me-mordam.txt') as arquivo:
    conteudo=arquivo.read()
    
i=0
a=[]
for d in conteudo:
    a.append(d.lower())
for x in a:
    if a=='banana':
        i+=1
print(i)
        