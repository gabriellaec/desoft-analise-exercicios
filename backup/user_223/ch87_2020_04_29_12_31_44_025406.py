with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    custo = 0
    for linha in linhas:
        separado = linha.split(',')
        for e in separado:
            custo+=(e[1]*e[2])
    print (custo)