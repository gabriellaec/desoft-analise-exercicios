with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
 
loop = True
i=0
while loop:
    if conteudo.lower().find('banana') != -1:
        conteudo.lower().replace('banana', 's')
        i+=1
    else:
        loop = False

print(i)