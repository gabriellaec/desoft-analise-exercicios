def verifica_progressao(lista):
    r=lista[1]-lista[0]
    q=lista[1]/lista[0]
    if lista[-1]=lista[0]+(len(lista)-1)*r:
        return "PA"
    elif lista[-1]=lista[0]*q**(len(lista)-1):
        return "PG"
    elif lista[-1]=lista[0]+(len(lista)-1)*r and lista[-1]=lista[0]*q**(len(lista)-1):
        return "AG"
    else:
        return "NA"