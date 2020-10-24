def classifica_lista(n):
    if n == []:
        print('nenhum') 
    if len(n)<2:
        print('nenhum') 
    for i in n:
        if n==sorted(n):
            print('crescente') 
        if n==sorted(n, reverse=True):
            print('decrescente')           
        else:
            print('nenhum') 