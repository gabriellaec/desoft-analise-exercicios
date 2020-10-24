def classifica_lista(lista):
    v=0
    f=100000000
    if lista==[] or len(lista)==1:
        return 'nenhum'
    for i in lista:
        if i>v:
            v=i
            return 'crescente'
        elif i<f:
            v=f
            return 'decrescente'
        else:
            return 'nenhum'

            
           