with open ('churras.txt', 'r') as churrastxt:
    conteudochurras = churrastxt.read()
with open ('churras.csv', 'w') as churrascsv:
    churrascsv.write(conteudochurras)
    linhas = churrascsv.readlines()
    custo = 0
    for linha in linhas:
        for e in linha:
            custo.append(e[1]*e[2])
            custototal = sum(custo)
    print (custototal)