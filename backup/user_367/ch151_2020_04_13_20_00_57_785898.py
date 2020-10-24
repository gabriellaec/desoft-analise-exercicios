def classifica_lista(y):
    y=[]
    return y
i=0
while i< len(y):
    if y == sorted(y):
        print('crescente')
    elif y == (sorted(reverse(y))):
        print('decrescente')
    else:
        print ('nenhum')
    i+=1