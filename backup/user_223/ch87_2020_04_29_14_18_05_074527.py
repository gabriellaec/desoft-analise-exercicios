with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    print (linhas)
    custo = 0
    for linha in linhas:
        print (linha)
        sem_espaco = linha.strip()
        separa = sem_espaco.split(',')
        print (separa)
    i = 0
    while i < len(linhas):
        for e in separa:
            e1=float(e[1])
            e2=float(e[2])
            custo+=(e1*e2)
        print (custo)