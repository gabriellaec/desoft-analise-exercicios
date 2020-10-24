def verifica_progressao(n):
    i=len(n)
    for o in range(len(n)):
        if n[i-o]==0 or n[i]==0:
                if n[i]-n[i-o]==n[i+o]-n[i]:
                    return ("PA")
                else:
                    return ("NA")
        if n[i]/n[i-o]==n[i+o]/n[i]:
            if n[i]-n[i-o]==n[i+o]-n[i]:
                return ("AG")
            else:
                return ("PG")
        else:
            if n[i]-n[i-1]==n[i+1]-n[i]:
                return ("PA")
            else:
                return ("NA")