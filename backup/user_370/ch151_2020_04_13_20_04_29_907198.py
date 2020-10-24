def classifica_lista(lista):
    i=1
    for i in lista:
        if lista[i+1]>lista[i]:
            print ("crescente")
        elif lista[i]>lista[i+1]:
            print ("decrescente")
        elif lista[i+1]>lista[i] and lista[i]>lista[i+1]:
            print ("nenhum")
        elif len(lista)< 2:
            print ("nenhum")
        i+=1

print(classifica_lista([1,2,4,6,8,9,10]))
            