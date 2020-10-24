def verifica_progressao(x): 
    for i in (x):
        if (i +1)/i == (i+2)/(i+1):
            return "PG"
        if (i +1)-i == (i+2)-(i+1):
            return "PA"
        if (i +1)/i == (i+2)/(i+1): and (i +1)-i == (i+2)-(i+1):
            return "AG"
        else:
            return "NA"