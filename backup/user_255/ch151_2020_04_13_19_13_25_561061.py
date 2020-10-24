lista=[]
def classifica_lista(lista):
    i=0
    s=1
    while i<len(lista):
        if lista[i]<lista[s]:
            print ('crescente')
        elif lista[i]>lista[s]:
            print ('decrescente')
        else:
            print ('nenhum')
        i+=1
        s+=1
        