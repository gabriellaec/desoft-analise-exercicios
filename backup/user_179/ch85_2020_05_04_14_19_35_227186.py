with open('macacos-me-mordam.txt', 'r') as texto:
    conteudo = texto.read()
    
conteudo.lower()    
palavras = conteudo.split()

i = 0
contador = 0
while i < len(palavras):
    if 'banana' == palavras[i]:
        contador = contador + 1
        i = i + 1
    else:
        i = i + 1
        
print(contador)