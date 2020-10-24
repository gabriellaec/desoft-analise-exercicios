def verifica_progressao(lista):
    r= lista[1]-lista[0]
    i=0
    for i in range(len(lista)):
        if lista[i+1]-lista[0]==r:
            return 'PA'
        
        
        