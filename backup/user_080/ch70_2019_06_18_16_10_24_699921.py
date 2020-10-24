def esconde_senha(string):
    tam=len(string)
    lista=[]
    i=0
    while i < tam:
        lista.append('*')
        i+=1
    return "".join(lista)