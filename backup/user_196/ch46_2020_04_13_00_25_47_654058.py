#def numero_no_indice(a):
    #lista = [1,3,2,4]
    #c = []
    #while a != lista[a]:
        #return False
        #a+=1
    #while a == lista[a]:
        #return True
        #c.append(a) 
        #return c
    #return c
def numero_no_indice(a):
    listanova =[]
    for i in range (len(a)):
        if a[i]==i:
            listanova.append(a[i])
    return listanova