def verifica_progressao(n):
    i=0
    while i < len(n):
        i += 1
        if n[i]-n[i-1]==n[i+1]-n[i] and n[i]/n[i-1]==n[i+1]/n[i]:
            c="AG"
        elif n[i]/n[i-1]!=n[i+1]/n[i]:
            c="PA"
        elif n[i]-n[i-1]!=n[i+1]-n[i]:
            c="PG"
        elif n[i]-n[i-1]!=n[i+1]-n[i] and n[i]/n[i-1]!=n[i+1]/n[i]:
            c="NA"
        return c
    