def classifica_lista(lista):
    a = len(lista)
    c = 0
    x = 0
    if a == 0:
        return 'nenhum'
    if a == 1:
        return 'nenhum'
    for i in range(a - 1):
        while c < a :
            if lista[i] < lista[i + 1]:
                return 'crescente'
                x = a + 100000
                c += 1
            else:
                c = a + 1000000
                x = 0
        while x < a:
            if lista[i] > lista[i + 1]:
                return 'decrescente'
                x += 1
            else:
                x = a + 1000
                return 'nenhum'
                
                
            
