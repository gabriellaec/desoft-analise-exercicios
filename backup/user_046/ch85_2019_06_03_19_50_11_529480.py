a=[]
i=0
with open('macacos-me-mordam.txt') as arquivo:
    conteudo=arquivo.read()
for d in conteudo:
   a.append(d.lower())
for x in a:
    if x=='banana':
        i+=1
print(i)

        