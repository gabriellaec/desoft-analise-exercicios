def verifica_progressao(n):
    i=2
    if n[i]/n[i-1]==n[i+1]/n[i]==n[i+2]/n[i+1]:
        if n[i-1]==0 or n[i]==0 or n[i+1]==0:
            if n[i]-n[i-1]==n[i+1]-n[i]==n[i+2]-n[i+1]:
                return ("PA")
            else:
                return ("NA")
        if n[i]-n[i-1]==n[i+1]-n[i]==n[i+2]-n[i+1]:
            return ("AG")
        else:
            return ("PG")
    else:
        if n[i]-n[i-1]==n[i+1]-n[i]==n[i+2]-n[i+1]:
            return ("PA")
        else:
            return ("NA")