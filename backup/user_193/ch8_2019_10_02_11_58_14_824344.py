def verifica_progressao(l):
    i=0
    while i<len(l)-2:
        if (l[i]+l[i+2])/2 == l[i+1] and (l[i]*l[i+2])**(1/2) == l[i+1]:
            return "AG"
        elif (l[i]+l[i+2])/2 == l[i+1]:
            return "PA"
        elif (l[i]*l[i+2])**(1/2) == l[i+1]:
            return "PG"
        else:
            return "NA"
        i+=1
        
        
xablau=[132,169,206,10]
print (verifica_progressao(xablau))