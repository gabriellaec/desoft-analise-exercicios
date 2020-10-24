
def verifica_progressao(n): 
    i=0
    x=n[i+1]-n[i]
    y=n[i+1]/n[i]
    while i+2<len(n):
        if x==n[i+2]-n[i+1] and y==n[i+2]/n[i+1]:
            s='AG'
        elif x==n[i+2]-n[i+1]:
            s='PA'
        elif y==n[i+2]/n[i+1]:
            s='PG'
        else:
            s='NA'
        i+=1
    return s     
    
        