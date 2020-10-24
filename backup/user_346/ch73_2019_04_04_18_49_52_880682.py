def remove_vogais(string):
    i=0
    string=list(string)
    while i<len(string):
        if string[i]=="a" or string[i]=="u" or string[i]=="o" or string[i]=="e" or string[i]=="i":
            del(string[i])
        else:
            i+=1
    lista1=[]
    lista1="".join(string)
    return lista1