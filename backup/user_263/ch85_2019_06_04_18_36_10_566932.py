with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()

conteudo = conteudo.split()
print(conteudo)

new = []
for palavras in conteudo:
    x = palavras.lower()
    new.append(x)
    
contador = 0
for palavra in new:
    if palavra == 'banana':
        contador += 1
        
print(contador)