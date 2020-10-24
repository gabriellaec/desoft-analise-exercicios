def verifica_progressao(lista):
    x = lista
    a = 0
    i =0
    r = a[i+1] - a[i]
    q = a[i+1]/a[i]
    if x[i+1]-x[i] == r  :
        return'PA'
    elif x[i+1]/x[i] == q:
        return "Pg"
    else:
        return "NA"


print(verifica_progresssao(lista))