def verifica_progressao(lista):
    i=0
    x=n[i]-n[i+1]
    y=n[i]/n[i+1]
    for i in lista:
        if x==n[i+1]-n[i+2] and y==n[i+1]/n[i+2]:
            return "AG"
        elif x==n[i+1]-n[i+2]:
            return "PA"
        elif y==n[i+1]/n[i+2]:
            return "PG"
        else:
            return "NA"

       
            
        