arquivo=open("macacos-me-mordam.txt")
conteudo=arquivo.read()
conteudo_novo=conteudo.split()


i=0
for x in conteudo_novo:
    ii=x.lower()
    if ii=="banana":
    	i=i+1
print(i)
                