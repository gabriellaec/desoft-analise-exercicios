def verifica_progressao(lista):
    for i in range(1,len(lista)):
        if 2*lista[i]==lista[i+1]+lista[i-1]:
            return 'PA'
        elif lista[i]**2==lista[i+1]*lista[i-1]:
            return 'PG'
        elif 2*lista[i]==lista[i+1]-lista[i-1] and lista[i]**2==lista[i+1]*lista[i-1]:
            return 'AG'
        else:
            return 'NA'
cacilda=[1,2,3]
print(verifica_progressao(cacilda))