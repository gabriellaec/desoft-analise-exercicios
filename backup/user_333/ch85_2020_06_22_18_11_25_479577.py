with open('macacos-me-mordam.txt','r') as arq:
    conteudo = arq.read()
    
minusculo = conteudo.lower()
quantidade = minusculo.count('banana')
print(quantidade)