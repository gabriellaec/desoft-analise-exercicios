
def verifica_progressao(n): 
    i=0
    x=n[i]-n[i+1]
    y=n[i]/n[i+1]
    if x==n[i+1]-n[i+2] and y==n[i+1]/n[i+2]:
        return 'AG'
    elif x==n[i]-n[i+1] and x==n[i+1]-n[i+2]:
        return 'PA'
    elif y==n[i+0]/n[i+1] and y==n[i+1]/n[i+2]:
        return 'PG'
    else:
        return 'NA'
    
        