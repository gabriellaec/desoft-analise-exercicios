with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
x=conteudo.lower()
num=x.find('banana')
print(num)