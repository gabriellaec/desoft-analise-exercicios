with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
b=conteudo.lower()
a=b.split()
nova=[]    

for i in range(len(a)):
    if a[i]=='banana':
        nova.append(a[i])
        print(a)