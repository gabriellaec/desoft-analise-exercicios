n= []
def soma_valores (n):
    i=0
    while i<= len(n) :
        n= n[i-1]+ n[i]
        i+=1
    return n