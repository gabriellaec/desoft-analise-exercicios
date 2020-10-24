def esconde_senha(string):
    n=len(string)
    lista=[]
    i=0
    while i<n+1:
        lista.append('*')
        i+=1
    return lista