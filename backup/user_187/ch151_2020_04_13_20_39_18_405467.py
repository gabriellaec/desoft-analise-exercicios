def classifica_lista(n):
    n=[]
    x=len(n)
    while x >= 2  :
        if n[1]-n[0] > 0 :
            print ('crescente')
        elif n[1]-n[0] < 0 :
            print ('decrescente')
        else :
            print ('nenhum') 
print ('nenhum ')        
