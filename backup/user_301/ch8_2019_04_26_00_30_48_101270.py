def verifica_progressao(lista):
    a=lista[1]-lista[0]
    pa=True
    for e in range(len(lista)):
        x=lista[e+1]-lista[e]
        if x!=a:
            pa=False
    b=lista[1]/lista[0]
    pg="verdadeiro"
    for i in range(len(lista)):
        y=lista[i+1]/lista[i]
        if y!=b:
            pg="falso"
    if pa==False and pg=="falso":
        return 'NA'
    if pa==False and pg=="verdadeiro":
        return "PG"
    if pa==True and pg =="falso":
        return "PA"
    if pa==True and pg=="verdadeiro":
        return "AG"
    