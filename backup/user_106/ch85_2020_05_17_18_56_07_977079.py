with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    
with open ('macacos-me-mordam.txt', 'w') as arquivo:
    conteudo.write(conteudo.lower())
    num=conteudo.find('banana')
    print(num)