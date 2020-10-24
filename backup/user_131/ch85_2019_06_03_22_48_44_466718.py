with open('macacos-me-mordam.txt','r') as arquivo: 
    conteudo = arquivo.read()
novo_conteudo = conteudo.upper()
m = novo_conteudo.split()
s = 0
for e in m:
    if e == 'BANANA':
        s +=s
        
print(s)

