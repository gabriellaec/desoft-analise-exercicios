def verifica_progressao(x):
    i = 0 
    while i < len(x):
        if x[i +1]/ x[i] == x[i+2]/x[i+1]:
            return "PG"
        if x[i +1]- x[i] == x[i+2]-x[i+1]:
            return "PA"
        if x[i +1]/ x[i] == x[i+2]/x[i+1] and x[i +1]- x[i] == x[i+2]-x[i+1]:
            return "AG"
        else:
            return "NA"