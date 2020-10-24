def classifica_lista(lista):
    n = len(lista)
    i = 0 
    i+=1
    while i <= n:
        if lista[i-1] < lista[i]:
      
            print('crescente')
        elif lista[i-1] > lista[i]:
            
            print('decrescente')
        else:
            print('nenhum')
    if n < 2:
        return('nenhum')
    