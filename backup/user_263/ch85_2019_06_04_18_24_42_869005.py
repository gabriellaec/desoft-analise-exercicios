with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()

conteudo = conteudo.split()
for palavras in conteudo:
    palavra.lower()
    
contador = 0
for palavra in conteudo:
    if palavra == 'banana':
        contador += 1
        
print(contador)