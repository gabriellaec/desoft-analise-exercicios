with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    novo=conteudo.lower()
    
with open ('macacos-me-mordam.txt', 'w') as arquivo:
    conteudo.write(novo)
    num=conteudo.find('banana')
    print(num)