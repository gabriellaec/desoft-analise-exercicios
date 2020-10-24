def verifica_progressao(a):
    if a[1]/a[0] == a[2]/a[1] and a[1] -a[0] == a[2] - a[1]:
        return "AG"
    elif a[1]/a[0] == a[2]/a[1]:
        return "PG"
    elif a[1] -a[0] == a[2] - a[1]:
        return "PA"
    else:
        return "NA"
    
    
    