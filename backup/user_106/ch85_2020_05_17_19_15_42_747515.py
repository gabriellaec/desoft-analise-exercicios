with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    x=conteudo.lower()
        
with open ('macacos-me-mordam.txt', 'w') as arquivo:
    arquivo.write(x)
    num=x.find('banana')
    print(num)