def verifica_progressao(lista):
    if lista[0]==0:
        return 'NA'
    razaopa=lista[1]-lista[0]
    razaopg=(lista[1]/lista[0])

 

    for i in range (1,len(lista)):
        if (lista[i+1]-lista[i])==razaopa and (lista[i+1]/lista[i])==razaopg:
            return 'AG'
        else:
            if lista[i+1]-lista[i]==razaopa and lista[(len(lista)-1)]-lista[(len(lista)-2)]==razaopa:
                return 'PA'
            elif lista[i+1]/lista[i]==razaopg and lista[(len(lista)-1)]/lista[(len(lista)-2)]==razaopg:
                return 'PG'
            else:
                return 'NA'