with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    resposta1 = conteudo.count('banana')
    resposta2 = conteudo.count('BANANA')
    resposta3 = conteudo.count('BaNaNa')
print(resposta1+reposta2+resposta)