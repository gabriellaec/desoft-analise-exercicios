
def verifica_progressao(n): 
    n=[]
    x=n[0]-n[1]
    y=n[0]/n[1]
    if x==n[1]-n[2] and y==n[1]/n[2]:
        return 'AG'
    elif x==n[0]-n[1] and x==n[1]-n[2]:
        return 'PA'
    elif y==n[0]/n[1] and y==n[1]/n[2]:
        return 'PG'
    else:
        return 'NA'
    
        