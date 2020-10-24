with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    
i = 0
for x in conteudo.lower():
    if x == 'banana': 
        i+=1
print(i)