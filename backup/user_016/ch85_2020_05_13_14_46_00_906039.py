with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    aumento = conteudo.upper()
    resposta = aumento.count('BANANA')
print(resposta)