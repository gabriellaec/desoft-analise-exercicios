def lista_sufixos(palavra):
    n=len(palavra)
    lista=[]
    i=0
    while i<n:
        lista.append(palavra)
        palavra=palavra.replace(palavra[0],"")
        i+=1
    return lista