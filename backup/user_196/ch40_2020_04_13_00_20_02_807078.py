#a = [1, 2, 3, 4]

#def soma_valores(a):
    #i = 0
    #soma_valores = 0
    #b = len(a)
    #while i < b:
        #soma_valores += a[i]
        #i+=1
    #return soma_valores

def soma_valores(a):
    somavalores = 0
    for i in range (len(a)):
        somavalores += a[i]
        print (somavalores)
    return somavalores