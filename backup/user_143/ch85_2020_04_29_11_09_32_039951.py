with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
c=conteudo.split()
a=0
for i in c:
    if len(i)==5 and i[1]=='a' or i[1]=='A' and i[4]=='n' or i[4]=='N':
        a+=1
print(a)
        