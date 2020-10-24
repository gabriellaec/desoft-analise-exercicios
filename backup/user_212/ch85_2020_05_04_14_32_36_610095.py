with open ('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    
novo_texto=conteudo.lower()

palavras=novo_texto.split

ocorre=0
for p in palavras:
    if p == 'banana':
        ocorre +=1
        
print (ocorre)        