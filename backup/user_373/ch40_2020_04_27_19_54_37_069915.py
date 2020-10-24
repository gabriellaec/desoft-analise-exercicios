n= []
i=0
def soma_valores (n):
    while i<= n:
        n= n[i-1]+ n[i]
        i+=1
    return n