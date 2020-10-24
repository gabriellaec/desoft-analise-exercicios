with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    print (linhas)
    custo = 0
    linha_de_linhas = []
    for linha in linhas:
        print (linha)
        sem_espaco = linha.strip()
        print(sem_espaco)
        linha_de_linhas.append(sem_espaco.split(','))
    print (linha_de_linhas)
    for linhas_sem_espaco in linha_de_linhas:
        print(linhas_sem_espaco)
        e1=float(e[1])
        e2=float(e[2])
        custo+=(e1*e2)
        print (custo)