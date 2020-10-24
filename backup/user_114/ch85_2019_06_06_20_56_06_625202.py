arquivo=open(macacos-me-mordam.txt)
conteudo=arquivo.read()
conteudo_novo=conteudo.split()
i=0
contador=0
while i<len(conteudo_novo):
    if h[0]=="B" or "b":
        if h[1],h[3],h[5]=="A" or "a":
            if h[2],h[4]=="N" or "n":
                contador=contador+1
    i=i+1
print(contador)
                