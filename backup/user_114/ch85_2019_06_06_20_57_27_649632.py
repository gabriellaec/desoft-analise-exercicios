arquivo=open(macacos-me-mordam.txt)
conteudo=arquivo.read()
conteudo_novo=conteudo.split()
i=0
contador=0
while i<len(conteudo_novo):
    if conteudo_novo[i][0]=="B" or "b":
        if conteudo_novo[i][1],conteudo_novo[i][3],conteudo_novo[i][5]=="A" or "a":
            if conteudo_novo[i][2],conteudo_novo[i][4]=="N" or "n":
                contador=contador+1
    i=i+1
print(contador)
                