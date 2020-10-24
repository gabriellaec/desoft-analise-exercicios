def classifica_lista(y):
    y=[]
    if y == sorted(y):
        print('crescente')
    elif y == (sorted(reverse(y))):
        print('decrescente')
    else:
        print ('nenhum')
   