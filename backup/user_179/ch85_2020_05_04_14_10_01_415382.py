contador = 0
with open('macacos-me-mordam.txt', 'r') as texto:
    conteudo = texto.read()
    conteudo.lower()
    for banana in conteudo:
        contador += 1
        
print(contador)