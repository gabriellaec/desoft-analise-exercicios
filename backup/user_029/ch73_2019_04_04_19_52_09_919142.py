def remove_vogais(r):
    lista=[]
    for i in r:
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
            lista.append(i)
    p=''
    for i in lista:
        p+=i
    return p