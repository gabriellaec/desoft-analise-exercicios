with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    
match = "banana"
print(len(conteudo.split(match)) - 1)