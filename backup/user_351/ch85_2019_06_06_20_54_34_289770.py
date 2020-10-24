with open ("macacos-me-mordam.txt","r") as arquivo:
    conteudo = arquivo.read()
    conteudo=conteudo.lower()
    junto=conteudo.split()
    i = 0
for d in junto:
    if d == "banana":
    	i+=1
print (i)