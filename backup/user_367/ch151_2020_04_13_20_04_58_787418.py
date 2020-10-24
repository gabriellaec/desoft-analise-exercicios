def classifica_lista(y):
    y=[]
    return y
i=0
while i< len(classifica_lista):
    if classifica_lista == sorted(classifica_lista):
        print('crescente')
    elif classifica_lista == (sorted(reverse(classifica_lista))):
        print('decrescente')
    else:
        print ('nenhum')
    i+=1