#def conta_palavras(texto):
with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    contador = 0
    for palavra in palavras:
        if palavra.lower() == "banana" or if palavra.lower() == "banana.":
            i = i+1
print(i)

#print(conta_palavras('macacos-me-mordam.txt'))