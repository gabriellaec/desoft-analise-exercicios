with open('macacos-me-mordam.txt') as arquivo:
    conteudo=arquivo.read()
    s.uppercase(conteudo)
i+=1
for d in conteudo:
    if d=='BANANA':
        i+=1
print(i)
        