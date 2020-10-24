with open('macacos-me-mordam.txt') as arquivo:
    conteudo=arquivo.read()
    conteudo=conteudo.upper()
i+=1
a+=1
while a<len(conteudo):
    if d=='BANANA':
        i+=1
    a+=1
print(i)
        