def verifica_progressao(n):
    if n[1]-n[0]==n[2]-n[1] and n[1]/n[0]==n[2]/n[1]:
        c="AG"
    elif n[1]/n[0]!=n[2]/n[1]:
        c="PA"
    elif n[1]-n[0]!=n[2]-n[1]:
        c="PG"
    else:
        c="NA"
    return c