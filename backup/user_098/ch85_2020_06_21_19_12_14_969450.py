with open ('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
minus=conteudo.lower()
lista=minus.split()
i=0
for word in lista:
    if word=='banana' or word == 'banana.':
        i+=1
print(i)