def lista_caracteres(s):
    li=[]
    for i in s:
        if i not in li:
            li.append(i)
    return li