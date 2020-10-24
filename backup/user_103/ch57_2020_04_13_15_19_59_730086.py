def verifica_progressao(lista):
    i=1
    razaopa=lista[1]-lista[0]
    razaopg=int(lista[1]/lista[0])
    while i < (len(lista)):
        if (lista[i+1]-lista[i])==razaopa and (lista[i+1]/lista[i])==razaopg:
            return 'AG'
        else:
            if lista[i+1]-lista[i]==razaopa:
                return 'PA'
            elif lista[i+1]/lista[i]==razaopg:
                return 'PG'
            else:
                return 'NA'
        i+=1

print(verifica_progressao(lista))
print(lista)
        