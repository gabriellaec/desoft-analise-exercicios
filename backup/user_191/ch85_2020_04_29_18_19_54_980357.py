with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
    conteudo=conteudo.lower()
    x=0
    for i in range(len(conteudo)):
        if i=="banana":
           x+=1 
    print(x)