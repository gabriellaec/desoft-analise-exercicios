#a = []
#def soma_impares(a):
    #i=0
    #while i < len(a):
        #if a[i] % 2 != 0:
            #a.append(i)
            #i+=1
        #else:
            #i+=1
    #return a

def soma_impares(a):
    b=0
    for i in range (len(a)):
        if a[i] % 2 != 0:
            b+=a[i]
    return b