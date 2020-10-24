def verifica_progressao(x):
    if len(x)<3:
        return "AG"
    else:
        for i in range(len(x)+1):
            if x[i+1]-x[i]==x[i+2]-x[i+1]:
                return "PA"
            if  x[i+1]-x[i]:
                return "AG"
            elif x[i+1]/x[i]==x[i+2]/x[i+1]:
                return "PG"
            elif  x[i+1]-x[i]==x[i+1]/x[i]:
                return "AG"
            
               
            else:
                return "NA"