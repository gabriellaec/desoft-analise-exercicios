def classifica_lista(y):
    y=[]
    if y == sorted(y):
        print('crescente')
    elif y == (sorted(reverse(y))):
        print('decrescente')
    if y == 0 or len(y)> 2: 
        print ('nenhum')
   