def remove_vogais(s):
    a=[]
    a=list(s)
    lista_nova=[]
    i=0
    while i<len(a):
        if i == "a" or i == "e" or i == "o" or i == "i" or i == "u":
            i+=1
        elif i == "a" and i == "e" and i == "o" and i == "i" and i == "u":
            return " "
        else:
            lista_nova.append(a[i])
            i+=1
    b = "".join(lista_nova)
    return b
