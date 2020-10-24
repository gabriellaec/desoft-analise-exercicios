def lista_sufixos(palavra):
    lista=[]
    i=0
    while i<len(palavra):
        lista.append(palavra)
        palavra=palavra.replace(palavra[0],"")
        i+=1
    return lista