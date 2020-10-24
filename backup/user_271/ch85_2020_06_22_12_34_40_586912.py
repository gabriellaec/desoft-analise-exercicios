with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    x=conteudo.split()
    b=0
    for y in x:
        h=y.lower()
        if h == "banana":
            b+=1
print(b)