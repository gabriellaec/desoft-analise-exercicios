with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    custo = 0
    for linha in linhas:
        for e in linha:
            custo+=(e[1]*e[2])
    print (custo)