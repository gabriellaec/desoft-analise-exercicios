def classifica_lista(n):
    pri:'crescente'
    seg:'decrescente'
    terc:'nenhum'
    n=[]
    x=len(n)
    while x >= 2  :
        if n[1]-n[0] > 0 :
            return pri
        elif n[1]-n[0] < 0 :
            return seg
        else :
            return terc 
print ('nenhum ')        
