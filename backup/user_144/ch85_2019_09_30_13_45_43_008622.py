with open('macac0s-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.lower()
    split = conteudo.split()
    i = 0
for palavra in split:
    if palavra == 'banana':
        i+=1
print(i)
            
        