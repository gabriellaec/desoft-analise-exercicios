with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read
    conteudo.lower()
    x=[]
    x.append(arquivo.find("banana"))
    print(len(x))