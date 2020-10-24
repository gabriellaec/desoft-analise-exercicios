def verifica_progressao(l):
    i=0
    while i<len(l):
        if (l[i]+l[i+2])/2 == l[i+1]:
            return "PA"
        elif (l[i]*l[i+2])**(1/2) == l[i+1]:
            return "PG"
        elif l[i]+l[i+2]/2 == l[i+1] and l[i]*l[i+1] == l[i+2]:
            return "AG"
        else:
            return "NA"
        i+=1