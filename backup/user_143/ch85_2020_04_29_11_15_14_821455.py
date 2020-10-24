with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
c=conteudo.split()
a=0
for i in c:
    i.lower()
    if i=='banana':
        a+=1
print(a)
        