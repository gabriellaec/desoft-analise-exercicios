with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    custo = 0
    for linha in linhas:
        separado = linha.split(',')
        for e in separado:
            e1_int=int(e[1])
            e2_int=int(e[2])
            custo+=(e1_int*e2_int)
    print (custo)