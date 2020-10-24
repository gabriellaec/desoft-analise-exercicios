with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()

conteudo = conteudo.lower()
loop = True
i=0
while loop:
    if conteudo.find('banana') != (-1):
        conteudo.replace('banana', 's')
        i+=1
    else:
        loop = False

print(i)