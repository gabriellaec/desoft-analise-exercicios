with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
    conteudo=conteudo.lower()
    x=[]
    x.append(conteudo.find("banana"))
    print(len(x))