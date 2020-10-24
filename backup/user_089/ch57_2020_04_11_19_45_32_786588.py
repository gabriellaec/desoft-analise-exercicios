def verifica_progressao(x):
    i = 0 
    while i < len(x):
        if x[i +1]/ x[i] == x[i+2]/x[i+1]:
            return "PG"
        else:
            return "PA"
            