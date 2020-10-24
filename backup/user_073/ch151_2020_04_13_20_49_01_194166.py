def classifica_lista(n):
    if n == []:
        return'nenhum' 
    if len(n)<2:
        return'nenhum'
    for i in n:
        if n==sorted(n):
            return'crescente' 
        if n==sorted(n, reverse=True):
            return'decrescente'          
        else:
            return'nenhum' 