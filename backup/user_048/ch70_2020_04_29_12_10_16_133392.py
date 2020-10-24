def esconde_senha(string):
    n=len(string)
    lista=[]
    i=0
    while i<n:
        lista.append('*')
        i+=1
    x=" ".join(lista)
    return lista