def verifica_progressao(lista):
    r=lista[1]-lista[0]
    q=lista[2]/lista[1]
    if lista[-1]==lista[0]+(len(lista)-1)*r and lista[-1]==lista[0]*q**(len(lista)-1):
        return "AG"
    elif lista[-1]==lista[0]+(len(lista)-1)*r:
        return "PA"
    elif lista[-1]==lista[0]*q**(len(lista)-1):
        return "PG"
    else:
        return "NA"