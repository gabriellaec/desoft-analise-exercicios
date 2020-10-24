with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    custo = 0
    for linha in linhas:
        separado = linha.split(',')
        for e in separado:
            e1=float(e[1])
            e2=float(e[2])
            custo+=(e1*e2)
    print (custo)