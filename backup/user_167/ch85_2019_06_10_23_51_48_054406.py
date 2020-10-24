with open ('macacos-me-mordam.txt', 'r') as arquivo:
    texto=arquivo.read()
    x=conteudo.split()
i=0
for linha in x:
    if linha.upper()=='BANANA':
        i+=1
print (i)
        
        
    
    