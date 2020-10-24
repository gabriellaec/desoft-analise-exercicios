with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    novo=conteudo.upper()
    
with open ('macacos-me-mordam.txt', 'w') as arquivo:
    conteudo.write(novo)
    num=conteudo.find('BANANA')
    print(num)