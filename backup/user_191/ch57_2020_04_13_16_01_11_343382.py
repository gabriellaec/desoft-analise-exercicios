def verifica_progressao(n):
    i=1
    if n[i]/n[i-1]==n[i+1]/n[i]:
        if n[i]-n[i-1]==n[i+1]-n[i]:
            return ("AG")
        else:
            return ("PG")
    else:
        if n[i]-n[i-1]==n[i+1]-n[i]:
            return ("PA")
        else:
            return ("NA")