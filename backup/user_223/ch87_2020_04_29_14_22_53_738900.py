with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    print (linhas)
#    custo = 0
    linhas_sem_enter = linhas.replace('\n', '')
    for linha in linhas_sem_enter:
        print (linha)
#        sem_espaco = linha.strip()
#        separa = sem_espaco.split(',')
#        print (separa)
#        
#        for e in separa:
#            e1=float(e[1])
#            e2=float(e[2])
#            custo+=(e1*e2)
#    print (custo)